import requests
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("crypto.db")
cursor = connection.cursor()

# Uncomment to create the table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        symbol TEXT NOT NULL,
        price TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
""")


def add_data(name, symbol, price, updated_at):
    try:
        cursor.execute(
            "INSERT INTO crypto_prices (name, symbol, price, updated_at) VALUES (?, ?, ?, ?)",
            (name, symbol, price, updated_at),
        )
        connection.commit()
        return "Data has been added to crypto_prices"
    except Exception as e:
        return f"Error in adding data to table: {e}"


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
go = {"X-CMC_PRO_API_KEY": "5f127f99-3f49-494d-96bb-cc3b464a0cc2"}

response = requests.get(url, headers=go)

if response.status_code == 200:
    data = response.json()
    for coin in data["data"]:
        name = coin["name"]
        symbol = coin["symbol"]
        price = coin["quote"]["USD"]["price"]
        updated_at = coin["last_updated"]
        print(add_data(name, symbol, price, updated_at))
else:
    print("Failed to fetch data from CoinMarketCap API")

connection.close()
