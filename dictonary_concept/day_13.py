# `. Create a dictionary to store the names and ages of three friends.
# Example: {"Ravi": 20, "Anu": 21, "Karthik": 19}

# data = {
#     "ravi" : 19,
#     "Hariharan" : 20,
#     "Rajesh" : 23

# }
# print(data)

# 2. Write a program to print all keys in a dictionary.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# print(input.keys())

# 3. Write a program to print all values in a dictionary.

# data = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# print(data.values())

# 4. Access and print the value of a specific key from a dictionary.

# data = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }
# print(data["name"])
# print(data["age"])


# 5. Add a new key-value pair to an existing dictionary.
# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# input ["city"] = "chennai"

# print(input.keys())
# print(input.values())
# print(input["name"])
# print(input)
# print(input["city"])

# 6. Update the value of an existing key in a dictionary.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# input["age"] = 20
# print(input)

# 7. Remove a key-value pair from a dictionary using pop().
# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# after removing adding new value 
# input["age"] = 21

# removing
# input.pop("age")
# print(input)

# 8. Check if a specific key exists in a dictionary.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# if "department" in input:
#     print("It exists in a dictionary")
# else:
#     print("does not exist")

#     # return input
#     print (input)

# 9. Get the length (number of items) of a dictionary.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# print("Total length of this input is:", len(input))


# # 10. Write a program to loop through all key-value pairs in a dictionary.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }

# for key, value in input.items():
#     print(key, ":", value)

