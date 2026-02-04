import time
from config import INTERVAL, TAKE_PROFIT, STOP_LOSS
from trader import get_data, market_buy, market_sell
from indicators import apply_indicators
from strategy import buy_signal
from logger import log
# from trader import has_open_position



print("🚀 Bot iniciado")

in_position = False
buy_price = 0
qty = 0
#in_position = has_open_position()

# if in_position:
#     print("⚠️ Posição aberta detectada (BTC na carteira)")
# else:
#     print("✅ Nenhuma posição aberta")
    
while True:
    
    try:
        
        df = get_data(INTERVAL)
        df = apply_indicators(df)
        price = df.iloc[-1].close # Preço atual
        print(f"[{time.strftime('%H:%M:%S')}] Rodando | Preço BTC: {price}")

        price = df.iloc[-1].close

        if not in_position and buy_signal(df):
            buy_price, qty = market_buy()
            in_position = True
            print(f"[{time.strftime('%H:%M:%S')}] 🟢 COMPRA | Preço: {buy_price} | Qty: {qty}")
            log(f"COMPRA | Preço: {buy_price} | Qty: {qty}")


        if in_position:
            if price >= buy_price * (1 + TAKE_PROFIT):
                market_sell(qty)
                in_position = False
                print(f"[{time.strftime('%H:%M:%S')}] ✅ TAKE PROFIT | Preço: {price}")
                log(f"TAKE PROFIT | Preço: {price}")

            elif price <= buy_price * (1 - STOP_LOSS):
                market_sell(qty)
                in_position = False
                print(f"[{time.strftime('%H:%M:%S')}] 🛑 STOP LOSS | Preço: {price}")
                log(f"STOP LOSS | Preço: {price}")

        time.sleep(60)

    except Exception as e:
        print("Erro:", e)
        time.sleep(60)
