import requests

print("Hello user")
response = float(input("How much is the total purchase "))
tip = (5/100) * response
total = tip + response
print(f"You are to pay {total} in total, which include 5% tip")
reply_1 = str(input("Select payment type\n1. Joint-payment\n2. Single-payment\n>> ")).lower()
if reply_1 == 'joint-payment' or reply_1 == "1":
    reply_2 = int(input("How many of you are paying\n>"))
    total_per_person = total / reply_2
    print(f"Each person will pay ₦{total_per_person} each")
elif reply_1 == 'single-payment' or reply_1 == '2':
    print(f"You will pay ₦{total} for the purchase")


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {"X-CMC_PRO_API_KEY": "5f127f99-3f49-494d-96bb-cc3b464a0cc2"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for coin in data["data"]:
        name = coin["name"]
        symbol = coin["symbol"]
        price = coin["quote"]["USD"]["price"]
        updated_at = coin["last_updated"]
        # print(add_data(name, symbol, price, updated_at))
