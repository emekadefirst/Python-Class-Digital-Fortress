import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

sk = os.getenv("PAYSTACK_SECRET_KEY")

url = "https://api.paystack.co/transaction/initialize"

headers = {
    "Authorization": f"Bearer {sk}",
    "Content-Type": "application/json"
}

data = {"email": "customer@email.com", "amount": 50000 * 100}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
