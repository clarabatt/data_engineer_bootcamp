import datetime
import json
import os

from typing import List


class DataTypeNotSupportedForIngestion(Exception):
    def __init__(self, data) -> None:
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class DataWriter:
    def __init__(self, coin: str, api: str) -> None:
        self.coin = coin
        self.api = api
        self.filename = f"{self.api}/{self.coin}/{datetime.datetime.now()}.json"

    def _write_row(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "a") as f:
            f.write(row)

    def write(self, data: [List, dict]):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) + "\n")
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestion(data)

# data = DaySummaryApi(coin="BTC").getData(date=datetime.date(2021, 6, 29))
# writer = DataWriter("day_summary.json")
# writer.write(data)

# data = TradesApi("BTC").getData(since=datetime.datetime(2021, 6, 2), until=datetime.datetime(2021, 6, 3))
# writer = DataWriter("trades.json")
# writer.write(data)
