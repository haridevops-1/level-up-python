# # Check whether a string is a palindrome
# def is_palindrome(word):
#     rev_character = ""
#     for char in word:
#         # print(char)
#         rev_character = char + rev_character
#     if word == rev_character:
#         print("palindrome")
#     else:
#         print("not")
#     # print(rev_character)

# is_palindrome("level")
# is_palindrome("The sun rises in the east")

# IF vowels not print -> output: dctn



# def is_vowels(word):
#     result = ""
#     vowel = "aeiouAEIOU"
#     for char in word:
#         if char not in vowel:
#             result = result + char
        # else:
        #     result = result +word
#     print(result)
# is_vowels("education")
# is_vowels("malayalam")

# do not repeat same values output -> 10,20,30,40,50,60,70,80,90,100

# def is_repeat(num):
#     result = []
#     for i in num:
#         if i not in result:
#             result.append(i)
#     print(result)

# is_repeat([10,10,20,20,30,30,40,40,50,50,60,60,70,70,80,80,90,100,100])


## parentesis

# def is_parenthesis(word):
#     count = 0
#     for i in word:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -=1
#         if count < 0:
#             print("false", count)
#             return
#     if count == 0:
#         print("True", count)
#     else:
#         print("False", count)


# is_parenthesis("((()))")
# is_parenthesis(")))()")

# between two zeroes print numbers 

# def is_between(num):
#     count = 0
#     result = []
#     for i in num:
#         if i == 0:
#             count += 1
#         elif count == 1:
#             result.append(i)
#     print(result)



# is_between([1,2,0,2,3,4,5,6,7,0])



def min_max (nums):
    max= nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    for i in range(len(nums)):
        min = nums[0]
        if nums[i] < min:
            min = nums [i]
    print(max-min)
min_max([10,9,8,7,6,4,5])
        
    