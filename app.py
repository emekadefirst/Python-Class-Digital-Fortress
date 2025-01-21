import requests
from fastapi import FastAPI
app = FastAPI()


def fetch():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    go = {"X-CMC_PRO_API_KEY": "5f127f99-3f49-494d-96bb-cc3b464a0cc2"}

    response = requests.get(url, headers=go)
    source = []
    if response.status_code == 200:
        data = response.json()
        for coin in data["data"]:
            name = coin["name"]
            symbol = coin["symbol"]
            price = coin["quote"]["USD"]["price"]
            updated_at = coin["last_updated"]
            new_data = {
                "name": name,
                "symbol": symbol,
                "price": price,
                "updated_at": updated_at
            }
            source.append(new_data)       
    return source

@app.get("/")
def main():
    return fetch()
