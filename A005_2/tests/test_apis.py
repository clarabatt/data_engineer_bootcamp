import datetime
import pytest
from apis import DaySummaryApi


@pytest.mark.parametrize(
    "coin, date, expected",
    [
        ("BTC", datetime.date(2021, 6, 21), "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21"),
        ("ETH", datetime.date(2021, 6, 21), "https://www.mercadobitcoin.net/api/ETH/day-summary/2021/6/21"),
        ("ETH", datetime.date(2019, 1, 2), "https://www.mercadobitcoin.net/api/ETH/day-summary/2019/1/2"),
    ]
)
def test_get_endpoint(coin, date, expected):
    api = DaySummaryApi(coin=coin)
    actual = api._get_end_point(date=date)
    assert actual == expected

