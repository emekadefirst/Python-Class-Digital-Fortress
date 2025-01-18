import requests

response = requests.get("https://dummyjson.com/products")
products = response.json()

for product in products['products']:
    print(f"Product with {product['id']} and name {product['title']} cost ${product['price']}")
