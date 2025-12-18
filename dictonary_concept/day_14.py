
# 1. Create an empty dictionary and add three key-value pairs using assignment (dict[key] = value).

# result = {}

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "sex" : "male"
# }

# result ["name"] = "Hariharan"
# result ["age"] = 21
# print(result)

# 2. Merge two dictionaries into one.

# a = {
#     "name" : "Rajesh",
#     "age" : 12
# }
# b = {
#     "name" : "chithra",
#     "age" : 13
# }

# merged = { ** a, ** b}
# print("merged is:", merged)

#3.  Write a program to get a value from a dictionary using get() method safely.

# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }
# print(input.get("name"))


# Clear all items from a dictionary using a method.


# input = {
#     "name" : "Hariharan",
#     "age" : 21,
#     "course" : "FSSA- student",
#     "education":{
#         "branch" : "ECE",
#         "year" : "2024"
#     }
# }
# input.clear()
# print(input)

# 5. Create a dictionary of 3 students with marks and print only those who scored above 50.
# students = {
#     "Rajesh" : 70,
#     "Hari" : 90,
#     "kamalesh": 21 
    
#     }

# for name, mark in students.items():
#     if mark > 50:
#         print(name, "scored High:", mark)

# 6. Write a program to count how many times each word appears in a sentence using a dictionary.

sentence = "I love python because python is easy and python is powerful"

sentence.split()

words_count = {}

for i in sentence:
    if i in words_count:
        words_count += 1
    else:
        words_count[i] = 1
print("Word count:", word_count)

# print(sentence)
# Create a nested dictionary (dictionary inside a dictionary) to store student info like name, age, and marks.

# Convert two lists — one of keys and one of values — into a dictionary.

# Write a program to copy a dictionary and show that changing one does not affect the other.