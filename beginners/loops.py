# while True:
#     name = input("Enter your name (type 'quit' to exit): ")
#     if name == "quit":
#         break
#     print("Hello, " + name + "!")

# x = 1
# while x < 3:
#     print(x)
#     x += 1
# else:
#     print("Loop completed")

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         break
#     print(i)


number_of_trial = 3
user_trial = 0
secrete_number = 7
print("Type quit to exit ")
while True:
    while user_trial < number_of_trial:
        response = int(
            input("Guess the number on my mind!! "))
        if response == secrete_number:
            print("Correct, You guessed right!!!")
            break
        else:
            print("NO You are WRONG!!!!!!!!!!!!")
            user_trial += 1  

    if user_trial == number_of_trial:
        print("Sorry, you've run out of trials!")
        reply = str(input("Type quit to end game"))
        if reply == "quit":
            break
