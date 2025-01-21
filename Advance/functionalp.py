## immutable functions
vu = "string"

xo = ("a", 1, True)

def append_to_tuple(tpl, value):
    return tpl + (value, )    

original_tuple = (1, 2, 3)
new_tuple = append_to_tuple(original_tuple, 4)

# print(new_tuple)


## pure funtion
def pure_function(a, b):
    return a + b

# print(pure_function(6, 5))


def conc_str(tpl, value):
    return f"{tpl} {value}"

string = "string"
# print(conc_str(string, "donation"))


## Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(100))


## Higher order function
def modulus(a, b):
    return a%b


def calc(func, value):
    return func(value)

## Non declarative style
data = list(range(0, 21))
new_data = []
for x in data:
    if x % 2 != 0:
        new_data.append(x)


print(new_data)

## Declarative style
numbers = list(range(0, 21))
odd_number = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_number)
