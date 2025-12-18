# Input:
# nums = [2, 7, 11, 15]
# target = 9
# Output:
# [0,1]


# def is_input(num, target):
#     sum = 0
#     for i in range(0,len(num)):
#         sum= sum + num[i]
#         if target == sum:
#             print(i)
# is_input([2,7,11,15], 9)


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# ```python
# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

# Input:  nums = [1,2,3,4]
# Output: False

### practicing for level-3 examination


# compare_print_g_b("APPLE", "APRON")
# GGBBB

# def is_print_g_b(a,b):
#     result = ""
#     for i in range (0,len(a),+1):
#         if a[i] == b[i]:
#             result = result + "G"
#         else:
#             result = result + "B"
#     print(result)


# is_print_g_b("APPLE", "APRON")


# # Reverse Words With Even Length
# # Reverse strings in a list only if their length is even.
# # Input: ["apple", "hi", "world", "cat"]
# #  Output: ["apple", "ih", "world", "cat"]

# def is_reverse(num):
#     result = []
#     for i in range(0,len(num),+1):
#         if i %2 == 0:
#             # value = num[i] + result
#             result.append(num[i])
#         else:
#             result.append(num[i])
#     print(result)

# is_reverse(["apple", "hi", "world", "cat"])


# def is_parenthesis(num):
#     count = 0
#     for i in range(len(num)):
#         if count < 0:
#             print("False")
#         if num[i] == "(":
#             count = count + 1
#         elif num[i] == ")":
#             count = count -1
#     if count == 0:
#         print("True")
#     else:
#         print("False")

# is_parenthesis("())")
    

# Write a Python program to:

# Find the average marks of male students.

# Find the average marks of female students.

# Print "Male <average>" if male students have the higher average, or "Female <average>" if female students have the higher average.

# For example:

# Test	Result
# find_higher_average(['M','F','M','F','M','F','M'],
#                     [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0]) 
# Male 85.0
# find_higher_average(['M','F','M','F','M','F','M'],
#                     [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])
# Female 80.0'''


# def is_calculating(gen_list,marks_list):
#     male_count = 0
#     male_marks = 0
#     female_count = 0
#     female_marks = 0
#     for i in range(0,len(gen_list),+1):
#         if gen_list[i] == "M":
#             male_marks = male_marks + marks_list[i]
#             male_count = male_count + 1
#         elif gen_list[i] == "F":
#             female_marks = female_marks + marks_list[i]
#             female_count = female_count +1
#     male_avg = male_marks / male_count
#     female_avg = male_marks / male_count
#     if male_avg > female_avg:
#         print(male_avg)
#     elif female_avg > male_avg:
#         print(female_avg)


# is_calculating(['M','F','M','F','M','F','M'],
# [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0]) 



'''Given a string "python" print all the characters in the even position,
 taking the first position as 1 and print it in reverse

1 2 3 4 5 6
p y t h o n  

For example:

Test	Result
str_rev_even("python")
output :nhy
'''

# def is_reverse(num):
#     result = ""
#     for i in range(len(num)-1,-1,-1):
#         if i % 2 == 0:
#             result = num[i] + result
#         else:
#             result = num[i]
#     print(result)

# is_reverse("python")

# # 2.Find the indices of numbers between the first 7 and second 7..Input:
# # [1, 7, 4, 3, 7, 9, 2, 7]
# # Output:
# # [2, 3]


# def is_between(num):
#     result = ""
#     for i in range(0,len(num),+1):
#         if num[i] == 7:
#             count = count +1
#             if count == 1:
                 


