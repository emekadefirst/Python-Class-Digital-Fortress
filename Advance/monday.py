import requests

url = "https://dummyjson.com/products"

response = requests.get(url)
print(response)
