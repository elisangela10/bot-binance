import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=3000, key="bot_status_refresh")



st.set_page_config(
    page_title="Bot Binance",
    layout="centered"
)

st.title("📈 Bot Binance – Painel de Controle  ")

STATUS_PATH = Path(__file__).parent.parent / "bot" / "bot_status.log"
st.divider()
st.subheader("🖥️ Status do Bot (tempo real)")



if STATUS_PATH.exists():
    
    with open(STATUS_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # mostra só as últimas 10 linhas
    last_lines = lines[-10:]

    st.code("".join(last_lines), language="text")
else:
    st.info("Status do bot ainda não disponível.")



CSV_PATH = Path(__file__).parent.parent / "bot" / "trade_history.csv"

# =========================
# Carregar histórico
# =========================
if not CSV_PATH.exists():
    st.warning("Nenhuma operação registrada ainda.")
    st.stop()

df = pd.read_csv(
    CSV_PATH,
    names=["datetime", "action", "price", "qty"]
)

if df.empty:
    st.warning("Arquivo existe mas não há dados.")
    st.stop()

df["price"] = df["price"].astype(float)
df["qty"] = df["qty"].astype(float)

# =========================
# Métricas
# =========================
buys = df[df["action"] == "BUY"]
sells = df[df["action"].str.contains("SELL")]

total_buy = (buys["price"] * buys["qty"]).sum()
total_sell = (sells["price"] * sells["qty"]).sum()
pnl = total_sell - total_buy

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 PnL Total (USDT)", f"{pnl:.2f}")
col2.metric("📊 Total Comprado", f"{total_buy:.2f}")
col3.metric("📉 Total Vendido", f"{total_sell:.2f}")
col4.metric("🔄 Trades", len(sells))

st.divider()

# =========================
# Status atual
# =========================
last_trade = df.iloc[-1]

if last_trade["action"] == "BUY":
    st.info(
        f"📌 Posição aberta | "
        f"Preço: {last_trade['price']} | "
        f"Qty: {last_trade['qty']}"
    )
else:
    st.success("✅ Nenhuma posição aberta")

st.divider()

# =========================
# Histórico
# =========================
st.subheader("📄 Histórico de Operações")
st.dataframe(df[::-1], use_container_width=True)
