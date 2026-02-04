import logging
from datetime import datetime  

STATUS_FILE = "bot/bot_status.log"

logging.basicConfig(
    filename="trades.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

def log(msg):
    with open("trades.log", "a") as f:
        f.write(msg + "\n")

def log_status(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    line = f"[{timestamp}] {message}"

    # imprime no console
    print(line)

    # grava no arquivo
    with open(STATUS_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")