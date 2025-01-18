# Threading and Async are module for excuting Concurrency in python code

# import threading


# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(50))


# thread = threading.Thread(target=factorial)
# thread.start()

# import pandas as pd


df = {
    "positive_word": ["like", "yes", "true", "good", "kind", "smile", "beautiful", "right", "gentle", "great", "nice"],
    "negative_word": ["dislike", "no", "false", "Bad", "Wicked", "frown", "ugly", "left", "wrong", "harsh", "poor"],
    "neutral_word": ["it", "is", "the", "this", "was", "in", "how", "that", "these", "where", "you", "are"],
}

pos = df["positive_word"]
neos = df["negative_word"]
nos = df["neutral_word"]
# for x in pos:
#     print(x)
# # print()

user_response = str(input("Enter your comment here: ")).lower().split()
print(user_response)


for x in user_response:
    if x in pos:
        print("positive statement")
        break
    elif x in neos:
        print("negative statement")
        break
    elif x in nos:
        print("neutral statement")
        break
    else:
        print("Unidentified statement")

