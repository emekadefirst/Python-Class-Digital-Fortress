import json
import requests

api_key = "sk_test_1f48e5677c58ed91157f9b207c14bdc493b398ad"
url = "https://api.paystack.co/transaction/initialize"
headers = {
    "Authorization": f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    "email": "divson404@gmail.com",
    "amount": 50000 * 100
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
