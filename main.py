import random


# secret_number = random.randint(1000, 9999)
# number_of_trials = 3
# guess_count = 0


# while guess_count < number_of_trials:
#     user_response = int(input("Guess the number on my mind\n> "))
#     if user_response == secret_number:
#         print("You're Amazing, you guessed right")
#         break
#     else:
#         print("Too bad!! you guessed wrong")
#     guess_count += 1

# def factorial(number):
#     if number == 0:
#         return 1
#     return number  * factorial(number-1)
# print(factorial(5))

class Vehicle:
    def __init__(self, brand, type, model, color, year, mileage, fuel_type, engin_type):
        self.brand = brand
        self.type = type
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.engine_type = engin_type
        
    def move(self):
        print("The car is moving ")
        
motor = Vehicle("Bugatti", "sport", "Cheron", "Andrew Tate Orange", 2014, "20000km", "Diesel","v8")
motor.move()