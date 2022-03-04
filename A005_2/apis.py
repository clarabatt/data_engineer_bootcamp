import datetime
import logging
import requests

from abc import abstractmethod
from backoff import on_exception
from ratelimit import limits, expo, exception

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MercadoBitcoinApi:
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.baseEndPoint = "https://www.mercadobitcoin.net/api"

    # Private method
    @abstractmethod
    def _get_end_point(self, **kwargs) -> str:
        pass

    @on_exception(expo, exception.RateLimitException, max_tries=10)
    @limits(calls=29, period=38)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_end_point(**kwargs)
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


# print(MercadoBitcoinApi(coin="BTC").getData())
# print(MercadoBitcoinApi(coin="LTC").getData())

class DaySummaryApi(MercadoBitcoinApi):
    type = 'day-summary'

    def _get_end_point(self, date: datetime.date) -> str:
        return f"{self.baseEndPoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}"


# print(DaySummaryApi(coin="BTC").getData(date=datetime.date(2021, 6, 21)))


def _get_unix_period(date: datetime.datetime) -> int:
    return int(date.timestamp())


class TradesApi(MercadoBitcoinApi):
    type = "trades"

    def _get_end_point(self, since: datetime = None, until: datetime = None) -> str:
        if since and not until:
            unix_since = _get_unix_period(since)
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}/{unix_since}"
        elif since and until:
            unix_since = _get_unix_period(since)
            unix_until = _get_unix_period(until)
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}/{unix_since}/{unix_until}"
        else:
            endpoint = f"{self.baseEndPoint}/{self.coin}/{self.type}"
        return endpoint

# print(TradesApi("BTC").getData())
# print(TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2)))
# print(TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2), until=datetime.datetime(2021, 6, 3)))
