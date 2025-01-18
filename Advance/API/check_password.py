import re
import string
import random as r

# upper = string.ascii_uppercase
# lower = string.ascii_lowercase
# punctuation = string.punctuation
# integers = string.digits


def check_password(password: str):
    password_pattern = ("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    match = re.match(password_pattern, string=password)
    return bool(match)


def generate_password():
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    punctuation = string.punctuation
    numbers = string.digits
    first_letter = "".join(r.sample(upper_letters, 4))
    second_letter = "".join(r.sample(lower_letters, 3))
    comma = "".join(r.sample(punctuation, 4))
    third_value = "".join(r.sample(numbers, 3))
    all_values = first_letter + second_letter + comma + third_value
    password = list(all_values)
    r.shuffle(password)
    shuffled_password = "".join(password)
    return shuffled_password

