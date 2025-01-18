# data.insert(0, 6)
# print(data[0:6])


# my_list = [1, 2, 3, 2, 4]
# my_list.remove(2)
# print(my_list)


# original_list = [1, 2, 3]
# copied_list = original_list.copy()
# print(copied_list)
# data = list(range(6))
# sqr = []
# for x in data:
#     value = x**2
#     sqr.append(value)

# print(sqr)


data = list(range(6))
sqr = list(map(lambda x: x**2, data))
print(sqr)


product = {
    "id": 1,
    "name": "Iphone 16 pro max",
    "price": 1599.96,
    "quantity": 25,
    "is_available": True,
}

product["quantity"] = 9
product.pop("quantity")

print(product)

# print(f"We have {product['quantity']} {product['name']} going for ${product["price"]} each currently available")
