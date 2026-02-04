import json

def save_position(price, qty):
    with open("position.json", "w") as f:
        json.dump({"price": price, "qty": qty}, f)

def load_position():
    try:
        with open("position.json") as f:
            data = json.load(f)
            return data["price"], data["qty"]
    except:
        return None, None
