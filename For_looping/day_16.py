##1
# num = int(input("Enter a number to check whether it is prime number or not:"))
# if num > 1:
#     for i in range (2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "It is a prime number")
# else:
#     print(num, "is not a prime number") 

# def score(a,b):
#     count = 0
#     for i in range(0,len(b)):
#         if b[i] > a[i]:
#             count = count + 1
#     print(count)
# score([45,60,70,55,80],[50,58,75,65,78])

#     2. Convert all spaces in a given sentence into - (without using in-built functions).
# ```python

# a = "Learn Python Easily"
# result = ""
# for i in range(0, len(a),+1):
#     if a[i] == " ":
#         result += "-"
#     else:
#         result += a[i]
# print(result)

# Input: "Learn Python Easily"
# Output: "Learn-Python-Easily"


# ```
# 4. Find Index of an Element (Without using index() or any in-built methods)
# Write a program to find the index position of a given number manually using loops.
# ```python
# Input:
# numbers = [11, 22, 33, 44, 55]
# search = 33
# Output: 2
# ```

# def is_search(a,b):
#         for i in range (0, len(a), +1):
#             if a[i] == b:
#                  print(i)
# is_search([11,22,33,44,55], 33)


#5. Given a value of n  print all the pattern in reverse if n = 7  , 7 # 5 # 3 # 1
# def is_reverse(n):
#       for i in range (n-0, -0, -1):
#             print(i)
# is_reverse(7)

# 6. Find the maximum between three numbers.

# def is_max_numbers(a,b,c):
#     if a >b and a > c:
#             print(a)
#     elif b >a and b > c:
#             print(b)
#     else:
#             print(c)

# is_max_numbers(3,4,5)
# 7. Given two positive check if their product is even or not.

def is_product(a, b):
       sum = a * b
       print(sum)
       if sum % 2 == 0:
              print("even")
       else:
              print("odd")
is_product(5,6)
is_product(9,8)


