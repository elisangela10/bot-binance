import pandas as pd
from config import FIXED_TRADE_USDT, client, SYMBOL, QTY_PERCENT

def get_data(interval):
    klines = client.get_klines(
        symbol=SYMBOL,
        interval=interval,
        limit=100
    )

    df = pd.DataFrame(klines, columns=[
        "time","open","high","low","close","volume",
        "ct","qav","nt","tb","tq","ignore"
    ])

    df["close"] = df["close"].astype(float)
    return df


def get_balance():
    balance = client.get_asset_balance(asset="USDT")
    return float(balance["free"])


def market_buy():
    usdt = get_balance()
    amount = usdt * QTY_PERCENT
    if amount < 10:
        raise Exception("Saldo insuficiente para operar (mínimo 10 USDT)")

    price = float(client.get_symbol_ticker(symbol=SYMBOL)["price"])
    qty = round(amount / price, 6)

    order = client.order_market_buy(
        symbol=SYMBOL,
        quantity=qty
    )
    return price, qty

def market_buy():
    usdt = get_balance()
    amount = FIXED_TRADE_USDT

    if usdt < amount:
        raise Exception("Saldo insuficiente para operar")

    price = float(client.get_symbol_ticker(symbol=SYMBOL)["price"])
    qty = round(amount / price, 6)

    client.order_market_buy(
        symbol=SYMBOL,
        quantity=qty
    )
    return price, qty


def market_sell(qty):
    client.order_market_sell(
        symbol=SYMBOL,
        quantity=qty
    )

# def has_open_position():
#     balance = client.get_asset_balance(asset="BTC")
#     return float(balance["free"]) > 0
