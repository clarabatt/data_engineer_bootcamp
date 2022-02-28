import datetime

from abc import ABC, abstractmethod
from apis import DaySummaryApi
from typing import List

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