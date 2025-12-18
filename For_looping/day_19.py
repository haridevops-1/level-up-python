# Unique Elements in Order
# Remove duplicates but maintain the original order.
# Example:
# Input: [1,2,3,1,2,4]
# Output: [1,2,3,4]

# def is_duplicate(input):
#     result = []
#     for i in range(0,len(input), +1):
#         if input[i] not in result:
#             result.append(input[i])
#     print(result)


# is_duplicate([1,2,2,3,3,4,4,5])

# Remove Vowels
# Remove all vowels from the string.
# Example:
# Input: "education"
# Output: "dctn"

# def is_vowels(val):
#     result = ""
#     vowels = "aeiouAEIOU"
#     for i in val:
#         if i not in vowels:
#             result = result + i
#     print(result)

# is_vowels("education") 
    
# Between Two Zeros
# Input: A list containing exactly two zeros.
# Print all the numbers between those two zeros (no slicing, no nested loops).
# Example:


# def is_between(int):
#     count = 0
#     result = []
#     for i in int:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             result.append(i)
#     print(result)


# is_between([1,2,0,2,3,4,5,6,0])


# Unique Elements in Order
# Remove duplicates but maintain the original order.
# Example:
# Input: [1,2,3,1,2,4]
# Output: [1,2,3,4]

# def is_duplicate(value):
#     result = []
#     for i in value:
#         if i not in result:
#             result.append(i)
#     print(result)


# is_duplicate([1,2,2,3,4,5,5,6])


# Count Frequency
# Print how many times each element appears in a list (without using collections.Counter).
# Example:
# Input: [2,2,3,4,3,3]
# Output:
# 2 -> 2 times
# 3 -> 3 times
# 4 -> 1 times

# def is_count(value):
#     count = 0
#     result = []
#     for i in value:
#         count +=1
#     print(count, i)

# is_count([1,2,2,2,22,2,3,4,5,])




# def is_between(input_string):
#     count = 0
#     result = []
#     for i in input_string:
#         if i == 0:
#             count += 1
#         elif count == 1:
#             result.append(i)
   
#     print(result)
    
# is_between([1,2,1,0,1,2,3,4,3,0])

# def is_parenthesis (input_string):
#     count = 0
#     for i in input_string:
#         if i == "(":
#             count +=1
#         elif i == ")":
#             count -=1
#         if count < 0:
#             print("false")
#             return
#     if count == 0:
#         print("True")
#     else:
#         print("False")

# is_parenthesis("(())")
# is_parenthesis("(((()")



# def is_common(input_string):
#     result = []
#     for i in input_string:
#         if i not in result:
#             result.append(i)
#     print(result)
# is_common([10,10,20,20,30,30,40,40,50,50,60,60,70,70])


# def is_vowels(word):
#     result = ""
#     vowel = "aeiou"
#     for i in word:
#         if i not in vowel:
#             result += i
#     print(result)


# is_vowels('education')



def is_palindrome(word):
    result = ""
    for i in word:
        result += i
    if result == word:
        print("palindrome", word)
    else:
        print("NOt", word)
        
    # print(result)
    
    
    
is_palindrome("level")