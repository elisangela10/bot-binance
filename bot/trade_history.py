import csv
from datetime import datetime

CSV_FILE = "bot/trade_history.csv"

def save_trade(action, price, qty):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            action,
            float(price),
            float(qty)
        ])
