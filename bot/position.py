import json

FILE = "bot/position.json"

def save_position(price, qty):
    with open(FILE, "w") as f:
        json.dump({"price": price, "qty": qty}, f)

def load_position():
    try:
        with open(FILE) as f:
            data = json.load(f)
            return data["price"], data["qty"]
    except:
        return 0, 0

def clear_position():
    open(FILE, "w").close()
