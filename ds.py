# pop
# my_list = list(range(11))
# print(my_list)
# print(my_list.pop())
# print(my_list)


# append
# my_list = list(range(11))
# my_list.append(3)
# print(my_list)

# clear
# my_list = list(range(11))
# my_list.clear()
# print(my_list)

# count
# my_list = list(range(11))
# print(my_list)
# my_list.append(3)
# print(my_list)
# print(my_list.count(3))

# extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)

# index
# my_list = [10, 20, 30, 20, 40]
# index_of_twenty = my_list.index(30)
# print(index_of_twenty)

# reverse and sort
# my_list = [2, 1, 5, 0, 3, 9, 6]
# my_list.sort()
# print(my_list)

# my_list.reverse()
# print(my_list)


# response = {
#     "id": 1,
#     "status": "Completed",
#     "mass": 45.98,
#     "is_valid": True
# }
# response["unit"] = 162 # add new entries
# response["mass"] = 50 # modify existing entry
# del response['status'] # delete entry
# response.pop("id") # pop existing entry
# print(response)
# print(response.values())
# print(response.keys())
# print(response.items())


# print(response["mass"])


# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[0])
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# my_tuple = ("a", "b")
# repeated_tuple = my_tuple * 34
# print(repeated_tuple)

# my_tuple = 1, 2, "hello"
# print(my_tuple)

my_tuple = (1, 2, "hello")
a, b, c = my_tuple
print(c)
