import datetime
import time 

from ingestors import DaySummaryIngestor
from writer import DataWriter
from schedule import every, run_pending, repeat

if __name__ == "__main__":
    daySummaryIngestor = DaySummaryIngestor(
        writer=DataWriter,
        coins=["BTC", "ETH", "LTC"],
        default_start_date=datetime.datetime(2021, 6, 1)
    )

    @repeat(every(1).seconds)
    def job():
        daySummaryIngestor.ingest()

    while True:
        run_pending()
        time.sleep(0.5)

