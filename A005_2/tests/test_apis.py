import datetime

from apis import DaySummaryApi


def test_get_endpoint_api_btc():
    date = datetime.date(2021, 6, 21)
    api = DaySummaryApi(coin="BTC")
    actual = api._get_end_point(date=date)
    expected = "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21"
    assert actual == expected


def test_get_endpoint_api_eth():
    date = datetime.date(2021, 6, 21)
    api = DaySummaryApi(coin="ETH")
    actual = api._get_end_point(date=date)
    expected = "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21"
    assert actual == expected

