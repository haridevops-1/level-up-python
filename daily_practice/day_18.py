# 1. Write a program to find the sum of all elements in a list.

# a = [10,20,30,40,50,60]
# sum = 0
# for i in range(0, len(a), +1):
#     sum += a[i]
# print("Total sum is:",sum)


# 2. Given a list of numbers, print only even numbers.

# num = [10,2,4,20,5,60,9,40,87]
# for el in range(0, len(num), +1):
#     if num[el] % 2 ==0:
#         print("It is even number:", num[el])
#     else:
#         print("Not even:", num[el])

# 3. Find the largest and smallest numbers in a list without using max() or min().

# value = [10,20,30,40,50,60]
# for el in value:
#     if value[el] > value[el+1]:
#         print("Highest") 


# 4. Count how many positive and negative numbers are in a list.
# num = [10,20,-12,-10,10,-90]
# count = 0
# sum = 0
# for i in range(0,len(num),+1):
#     if num[i] > 0:
#         count+=1
#     else:
#         sum+=1
# print("Negative:",sum)
# print("postive:",count)

# 5. Given a list of numbers, create a new list with each number squared.

# num = [10,20,30,40,50,60]
# b = []
# for i in num:
#     b.append(i*i)
# print(b)

# 🔡 String-based Questions

# Count how many vowels are present in a given string.
# a ="apple"
# vowels = 'aeiou'
# count = 0
# for i in range(0,len(a),+1):
#     if a[i] in vowels:
#         count +=1
# print(count)
        

# Reverse a string using a loop (don’t use slicing or built-in reverse).
# a = "hello world"
# b = ""
# for i in range(0,len(a), +1):
#     b = a[i] + b
# print(b)

# Count how many times a specific character appears in a string.
# a = [1,2,3,9,10]
# b = [1,2,3,4,5,6,7,8,9,10]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)
          

# Check whether a string is a palindrome (same forwards and backwards).
# def is_palindrome(n):
    # b = ""
    # for i in range((len(n))-1,-1,-1):
    #     b = b + n[i]
    # if b == n:
    #     print("True")
    # else:
    #     print("False")
# is_palindrome("level")
# 
# Convert a string to lowercase manually using a loop (without using .lower()).
a = "qwertyuiopasdfghjklzxcvbnm"
b = "KAMALESH"
c = ""
for i in b:
    if b in a:
        c += i
print(c)

    
