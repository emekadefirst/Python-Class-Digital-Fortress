# def greeting():
#     print("Hello, World!")

# greeting()


# def greeting():
#     return "index.html"

# def tip_calculator(cost):
#     tip = (5/100) * cost
#     return tip

# print(tip_calculator(90000))

# def modulus(a, b):
#     c = a % b
#     return c
# print(modulus(50, 3))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))