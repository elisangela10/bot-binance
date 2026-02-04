import pandas as pd
from config import client, SYMBOL, FIXED_TRADE_USDT


# =========================
# Dados de mercado
# =========================
def get_data(interval):
    klines = client.get_klines(
        symbol=SYMBOL,
        interval=interval,
        limit=100
    )

    df = pd.DataFrame(klines, columns=[
        "time", "open", "high", "low", "close", "volume",
        "ct", "qav", "nt", "tb", "tq", "ignore"
    ])

    df["close"] = df["close"].astype(float)
    return df


# =========================
# Saldo
# =========================
def get_usdt_balance():
    balance = client.get_asset_balance(asset="USDT")
    return float(balance["free"])


def get_btc_qty():
    balance = client.get_asset_balance(asset="BTC")
    return float(balance["free"])


def has_open_position():
    return get_btc_qty() > 0


# =========================
# Ordens
# =========================
def market_buy():
    usdt = get_usdt_balance()
    amount = FIXED_TRADE_USDT

    if usdt < amount:
        raise Exception("Saldo insuficiente para operar")

    price = float(client.get_symbol_ticker(symbol=SYMBOL)["price"])
    qty = round(amount / price, 6)  # BTCUSDT stepSize

    client.order_market_buy(
        symbol=SYMBOL,
        quantity=qty
    )

    return price, qty


def market_sell(qty):
    qty = round(qty, 6)

    if qty <= 0:
        raise Exception("Quantidade inválida para venda")

    client.order_market_sell(
        symbol=SYMBOL,
        quantity=qty
    )
    
def get_last_buy_price():
    trades = client.get_my_trades(symbol=SYMBOL, limit=50)

    # percorre do mais recente para o mais antigo
    for trade in reversed(trades):
        if trade["isBuyer"]:
            price = float(trade["price"])
            qty = float(trade["qty"])
            return price, qty

    return 0, 0
