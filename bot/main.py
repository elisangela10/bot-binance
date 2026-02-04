import time
import json
from pathlib import Path
from config import INTERVAL, TAKE_PROFIT, STOP_LOSS
from trader import (
    get_data,
    market_buy,
    market_sell,
    get_btc_qty,
    get_last_buy_price,
    get_usdt_balance
)
from indicators import apply_indicators
from strategy import buy_signal
from trade_history import save_trade
from logger import (log, log_status)




log_status("🚀 Bot iniciado")





CONTROL_FILE = Path("bot/bot_control.json")

def bot_is_enabled():
    if not CONTROL_FILE.exists():
        return False

    with open(CONTROL_FILE, "r") as f:
        data = json.load(f)

    return data.get("run", False)


# =========================
# Estado inicial
# =========================
buy_price = 0.0
qty = get_btc_qty()
in_position = qty > 0

if in_position:
    buy_price, _ = get_last_buy_price()

    if buy_price > 0:
        log_status(
            f"♻️ Recovery automático | "
            f"Preço entrada: {buy_price} | Qty BTC: {qty}"
        )
    else:
        log_status("⚠️ BTC detectado, mas não foi possível recuperar o preço de entrada")
else:
    log_status("✅ Nenhuma posição aberta")


# =========================
# Loop principal
# =========================
while True:
    if not bot_is_enabled():
        log_status("⏸️ Bot pausado pelo painel")
        time.sleep(5)
        continue
    try:
        df = get_data(INTERVAL)
        df = apply_indicators(df)

        price = float(df.iloc[-1].close)
        log_status(f"[{time.strftime('%H:%M:%S')}] Rodando | Preço BTC: {price}")

        # =========================
        # CASO 1 — JÁ ESTÁ EM POSIÇÃO → NUNCA COMPRA
        # =========================
        if in_position:
            qty = get_btc_qty()  # sempre usa saldo real

            # proteção Binance
            if qty * price < 10:
                log_status("⛔ Valor da posição abaixo do mínimo da Binance")
                time.sleep(60)
                continue

            # TAKE PROFIT
            if buy_price > 0 and price >= buy_price * (1 + TAKE_PROFIT):
                market_sell(qty)

                save_trade("SELL_TP", price, qty)
                log(f"TAKE PROFIT | Preço: {price}")

                log_status(
                    f"[{time.strftime('%H:%M:%S')}] ✅ TAKE PROFIT | "
                    f"Preço: {price}"
                )

                buy_price = 0
                in_position = False

            # STOP LOSS
            elif buy_price > 0 and price <= buy_price * (1 - STOP_LOSS):
                market_sell(qty)

                save_trade("SELL_SL", price, qty)
                log(f"STOP LOSS | Preço: {price}")

                log_status(
                    f"[{time.strftime('%H:%M:%S')}] 🛑 STOP LOSS | "
                    f"Preço: {price}"
                )

                buy_price = 0
                in_position = False

        # =========================
        # CASO 2 — NÃO ESTÁ EM POSIÇÃO → PODE COMPRAR
        # =========================
        else:
            usdt = get_usdt_balance()

            if usdt < 10:
                log_status("⛔ Sem USDT suficiente para comprar")
                time.sleep(60)
                continue

            if buy_signal(df):
                buy_price, qty = market_buy()
                in_position = True

                save_trade("BUY", buy_price, qty)
                log(f"COMPRA | Preço: {buy_price} | Qty: {qty}")

                log_status(
                    f"[{time.strftime('%H:%M:%S')}] 🟢 COMPRA | "
                    f"Preço: {buy_price} | Qty: {qty}"
                )

        time.sleep(60)

    except Exception as e:
        log_status("Erro:", e)
        time.sleep(60)

