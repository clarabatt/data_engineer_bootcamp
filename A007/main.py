# %%
# imports
import json

import requests

# %%
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
ret = requests.get(url)
if ret:
    print(ret.text)
else:
    print("falhou")
# %%
dolar = json.loads(ret.text)["USDBRL"]
print(f"20 dólares hoje custam {float(dolar['bid']) * 20} reais")


# %%
def cotacao(value, currency):
    url = f"https://economia.awesomeapi.com.br/last/{currency}"
    ret = requests.get(url)
    dolar = json.loads(ret.text)[currency.replace("-", "")]
    print(
        f"{value} {currency[:3]} hoje custam {float(dolar['bid']) * 20} {currency[-3:]}"
    )


# %%
cotacao(20, "USD-BRL")
cotacao(50, "BRL-JPY")
cotacao(50, "BRL-UYU")
# %%
try:
    cotacao(50, "clara")
except:
    pass
# %%
try:
    cotacao(50, "uahsuahs")
except Exception as e:
    print(e)
else:
    print("ok")
# %%

lst_currency = ["USD-BRL", "BTC-BRL", "BRL-UYU", "CAD-BR"]


def multi_currency(value, arr):
    for currency in arr:
        try:
            url = f"https://economia.awesomeapi.com.br/last/{currency}"
            ret = requests.get(url)
            cur = json.loads(ret.text)[currency.replace("-", "")]
            print(
                f"{value} {currency[:3]} hoje custam {float(cur['bid']) * 20} {currency[-3:]}"
            )
        except Exception as e:
            print(f"falha na moeda: {e}")


multi_currency(20, lst_currency)


# %%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")

    return inner_func


@error_check
def currency_now(value, currency):
    url = f"https://economia.awesomeapi.com.br/last/{currency}"
    ret = requests.get(url)
    cur = json.loads(ret.text)[currency.replace("-", "")]
    print(
        f"{value} {currency[:3]} hoje custam {float(cur['bid']) * 20} {currency[-3:]}"
    )


currency_now(20, "USD-BRL")
currency_now(50, "BRL-JPY")
currency_now(50, "BRL-UYU")

# %%
import backoff
import random


@backoff.on_exception(
    backoff.expo,
    (ConnectionAbortedError, ConnectionRefusedError, TimeoutError),
    max_tries=10,
)
def test_func(*args, **kargs):
    rnd = random.random()
    print(
        f"""
        RND: {rnd}
        args: {args if args else 'sem args'}
        kargs: {kargs if kargs else 'sem kargs'}
    """
    )
    if rnd > 0.2:
        raise ConnectionAbortedError("Conexão Finalizada")
    elif rnd > 0.4:
        raise ConnectionRefusedError("Conexão Recusada")
    elif rnd > 0.6:
        raise TimeoutError("Tempo exceditdo")
    else:
        return "OK!"


# %%
test_func()
test_func(42)
test_func(42, name="clara")

# %%
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


@backoff.on_exception(
    backoff.expo,
    (ConnectionAbortedError, ConnectionRefusedError, TimeoutError),
    max_tries=10,
)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND: {rnd}")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd > 0.2:
        log.error("Conexão Finalizada")
        raise ConnectionAbortedError("Conexão Finalizada")
    elif rnd > 0.4:
        log.error("Conexão Recusada")
        raise ConnectionRefusedError("Conexão Recusada")
    elif rnd > 0.6:
        log.error("Tempo excedido")
        raise TimeoutError("Tempo excedido")
    else:
        return "OK!"


# %%
test_func()
