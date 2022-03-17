import datetime
import pytest

from mercado_bitcoin.apis import DaySummaryApi, TradesApi


class TestDaySummaryAPI:
    @pytest.mark.parametrize(
        "coin, date, expected",
        [
            (
                "BTC",
                datetime.date(2021, 6, 21),
                "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21",
            ),
            (
                "ETH",
                datetime.date(2021, 6, 21),
                "https://www.mercadobitcoin.net/api/ETH/day-summary/2021/6/21",
            ),
            (
                "ETH",
                datetime.date(2019, 1, 2),
                "https://www.mercadobitcoin.net/api/ETH/day-summary/2019/1/2",
            ),
        ],
    )
    def test_get_endpoint(self, coin, date, expected):
        api = DaySummaryApi(coin)
        actual = api._get_endpoint(date=date)
        assert actual == expected


class TestTradesAPI:
    @pytest.mark.parametrize(
        "coin, since, until, expected",
        [
            (
                "TESTE",
                datetime.datetime(2019, 1, 1),
                datetime.datetime(2019, 1, 2),
                "https://www.mercadobitcoin.net/api/TESTE/trades/1546318800/1546405200",
            ),
            (
                "TESTE",
                datetime.datetime(2021, 6, 12),
                datetime.datetime(2021, 6, 15),
                "https://www.mercadobitcoin.net/api/TESTE/trades/1623470400/1623729600",
            ),
            ("TESTE", None, None, "https://www.mercadobitcoin.net/api/TESTE/trades"),
            (
                "TESTE",
                None,
                datetime.datetime(2021, 6, 12),
                "https://www.mercadobitcoin.net/api/TESTE/trades",
            ),
            (
                "TESTE",
                datetime.datetime(2021, 6, 12),
                None,
                "https://www.mercadobitcoin.net/api/TESTE/trades/1623470400",
            ),
        ],
    )
    def test_get_endpoint(self, coin, since, until, expected):
        actual = TradesApi(coin)._get_endpoint(since, until)
        assert actual == expected

    def test_get_endpoint_since_greater_than_until(self):
        with pytest.raises(RuntimeError):
            TradesApi("TESTE")._get_endpoint(
                datetime.datetime(2021, 6, 15), datetime.datetime(2021, 6, 12)
            )

    @pytest.mark.parametrize(
        "date, expected",
        [
            (datetime.datetime(2019, 1, 1), 1546318800),
            (datetime.datetime(2019, 1, 2), 1546405200),
            (datetime.datetime(2021, 6, 12, 0, 0, 5), 1623470405),
            (datetime.datetime(2022, 1, 1), 1641013200),
        ],
    )
    def test_get_unix_period(self, date, expected):
        actual = TradesApi("TESTE")._get_unix_period(date)
        assert actual == expected
