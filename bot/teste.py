from binance.client import Client
import os

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)

try:
    account = client.get_account()
    print("✅ API conectada com sucesso")
    print("Ativos na conta:")
    for asset in account["balances"]:
        if float(asset["free"]) > 0:
            print(asset)
except Exception as e:
    print("❌ Erro ao conectar na API")
    print(e)
