# def is_replace(odd):
#     result = ""
#     for i  in range(0,len(odd),+1):
#         if i % 2 == 1:
#             result = result + "*"
#         else:
#             result = result + odd[i]
#     print(result)
        
        
# is_replace("hello")

# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is


# def is_smallest(word):
    ##splitting word
    # result = word.split()
    ## declaring variable for comparing
    # smallest = result[0]
    ## running loop for result
    # for w in result:
        ## find through length
    #         if len(result) < len(smallest):
    #             smallest = w
    # print(smallest)
    
    
# is_smallest( "Python is super powerful")


# def is_comparison(num):
    ## looping
#     for w in range(0,len(num)-1):
#         if num[w+1] <= num[w]:
#             return False
#     return True
    
# print(is_comparison([1,2,3,4,5]))
# print(is_comparison([1,2,2,3,4,5]))



#  Sum of First and Last Elements
# Write a program to find the sum of the first and last elements of a list.
# python
# Input: [10, 20, 30, 40, 50]
# Output: 60  # (10 + 50)
# - Find Index of an Element (Without using index())

## method 1
def is_without_index(num):
     first = num[0]
     last = num[-1]

     result = first + last
     print("Final result is ->", result)


is_without_index([10,20,30,40,50])

##method 2

def is_using_target(num):
     target = 30
     index = -1
     for i in range(len(num)):
          if num[i] == target:
               index = i
               break
     print(num[i])


is_using_target([10,20,30,40,50,60])
               
#  Compare two lists and print a new list marking:

# "T" → if element sum is even

# "F" → if element sum is odd

# Example
# A = [1, 2, 3, 4]
# B = [4, 1, 6, 5]

# Output:
# ['F', 'T', 'T', 'T']
# (1+4=5 odd → F) (2+1=3 odd → F) etc.

# def is_compare(a,b):
#      result = []
#      for i in range(len(a)):
#           total = a[i] + b[i]
#           if total % 2 == 0:
#                result.append("T")
#           else:
#                result.append("F")
#      print(result)


# is_compare([1,2,3,4], [4,1,6,5])



# def longest_word_from_string(text):
#     words = text.split()     # convert string → list
#     longest = words[0]

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     print(longest)


# longest_word_from_string("apple banana kiwi strawberry")
