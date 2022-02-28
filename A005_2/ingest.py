from abc import ABC, abstractmethod
from asyncore import write
from typing import List
from unittest.util import strclass
from backoff import on_exception
from ratelimit import limits, expo, exception
from schedule import every, run_pending, repeat
import datetime
import json
import logging
import os
import requests
import time 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MercadoBitcoinApi():
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.baseEndPoint = "https://www.mercadobitcoin.net/api"

    # Private method
    @abstractmethod
    def _getEndPoint(self, **kwargs) -> str:
        pass

    @on_exception(expo, exception.RateLimitException, max_tries=10)
    @limits(calls=29, period=38)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def getData(self, **kwargs) -> dict:
        endpoint = self._getEndPoint(**kwargs)
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


# print(MercadoBitcoinApi(coin="BTC").getData())
# print(MercadoBitcoinApi(coin="LTC").getData())

class DaySummaryApi(MercadoBitcoinApi):
    type = 'day-summary'

    def _getEndPoint(self, date: datetime.date) -> str:
        return f"{self.baseEndPoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}"


# print(DaySummaryApi(coin="BTC").getData(date=datetime.date(2021, 6, 21)))


class TradesApi(MercadoBitcoinApi):
    type = "trades"

    def _getUnixPeriod(self, date: datetime.datetime) -> int:
        return int(date.timestamp())


    def _getEndPoint(self, since: datetime = None, until: datetime = None) -> str:
        if since and not until:
            unix_since = self._getUnixPeriod(since)
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}/{unix_since}"
        elif since and until:
            unix_since = self._getUnixPeriod(since)
            unix_until = self._getUnixPeriod(until)
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}/{unix_since}/{unix_until}"
        else:
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}"
        return endpoint


# print(TradesApi("BTC").getData())
# print(TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2)))
# print(TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2), until=datetime.datetime(2021, 6, 3)))

class DataTypeNotSupportedForIngestion(Exception):
    def __init__(self, data) -> None:
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)

class DataWritter():
    def __init__(self, coin: str, api: str) -> None:
        self.coin = coin
        self.api = api
        self.filename = f"{self.api}/{self.coin}/{datetime.datetime.now()}.json"

    def _writeRow(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "a") as f:
            f.write(row)

    def write(self, data: [List, dict]):
        if isinstance(data, dict):
            self._writeRow(json.dumps(data) + "\n")
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestion(data)


# data = DaySummaryApi(coin="BTC").getData(date=datetime.date(2021, 6, 29))
# writer = DataWritter("day_summary.json")
# writer.write(data)

# data = TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2), until=datetime.datetime(2021, 6, 3))
# writer = DataWritter("trades.json")
# writer.write(data)

class DataIngestor(ABC):
    def __init__(self, coins: List[str], defaulStartDate: datetime.datetime, writer) -> None:
        self.defaultStartDate = defaulStartDate
        self.coins = coins
        self.writer = writer
        self._checkpoint = self._loadCheckpoint()

    @property
    def _checkpointFilename(self) -> str:
        return f"{self.__class__.__name__}.checkpoint"

    def _saveCheckpoint(self):
        with open(self._checkpointFilename, "w") as f:
            f.write(f"{self._checkpoint}")

    def _loadCheckpoint(self) -> datetime.date:
        try:
            with open(self._checkpointFilename, "r") as f:
                return datetime.datetime.strptime(f.read(), "%Y-%m-%d").date()
        except FileNotFoundError:
            return None

    def _getCheckpoint(self):
        if not self._checkpoint:
            return self.defaultStartDate
        else: return self._checkpoint

    def _updateCheckpoint(self, value):
        self._checkpoint = value
        self._saveCheckpoint()
    
    @abstractmethod
    def ingest(self) -> None:
        pass


class DaySummaryIngestor(DataIngestor):

    def ingest(self) -> None:
        date = self._getCheckpoint()
        if date < datetime.date.today():
            for coin in self.coins:
                api = DaySummaryApi(coin=coin)
                data = api.getData(date=date)
                self.writer(coin=coin, api=api.type).write(data)
            self._updateCheckpoint(date + datetime.timedelta(days=1))

ingestor = DaySummaryIngestor(writer=DataWritter, coins=["BTC", "ETH", "LTC"], defaulStartDate=datetime.date(2021, 6, 1))

@repeat(every(1).seconds)
def job():
    ingestor.ingest()

while True:
    run_pending()
    time.sleep(0.5)