# 1. Count Vowels and Consonants
# Write a program to count how many vowels and consonants are in a given string.

# def is_count_vowels(value):
#     count  = 0
#     sum = 0
#     for i in value:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             count +=1
#         else:
#             sum += 1
#     print("The vowels count is: ", count)
#     print("The consonant's count is: ", sum)

# is_count_vowels("hello world")

# 2. Sum of Even and Odd Digits
# Given an integer, find the sum of its even digits and the sum of its odd digits separately.

# 2. Count Positive, Negative, and Zero Elements in a List
# Given a list of integers, count how many are positive, negative, or zero using loops.

# def is_counting(n):
#     positive = 0
#     negative = 0
#     zero = 0
#     for i in n :
#         if i > 0:
#             positive +=1
#         elif i < 0:
#             negative +=1
#         else:
#             zero +=1

#     print("Total count (+) =", positive)
#     print("Total count (-) =", negative)
#     print("Total count (0) =", zero)

# is_counting([1,2,3,7,89,0,0,0,-6,-4,-24,6])

# 3. Count Words Starting with a Vowel
# Given a sentence, count how many words start with a vowel (a, e, i, o, u).

# def is_vowel (num):
#     vowel = 0
#     for i in num:
#         # print(i)
#         if i == "a" or i =="e" or i == "i" or i == "o" or i == "u":
#             vowel += 1
#     print("Total count of vowels: ",vowel)

# is_vowel ("The sky is blue")

# 4. Find the Factorial of a Number

# def is_factorial(num):
#    fact = 1
#    for i in range (1, num+1, +1):
#       fact = fact * i
#    print(fact)

# is_factorial(5)

# P5. rint Multiplication Table of a Number
# Example: for 5 → 5×1=5, 5×2=10, …, 5×10=50

def is_multiplication(n):
    for i in range(1, 11):      
        print(n, "x", i, "=", n * i)

is_multiplication(5)
