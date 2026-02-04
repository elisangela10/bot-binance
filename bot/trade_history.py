import csv
from datetime import datetime

def save_trade(action, price, qty):
    with open("trade_history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            action,
            price,
            qty
        ])
