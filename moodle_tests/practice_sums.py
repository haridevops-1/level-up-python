## 1.
# def between(num):
#     result = []
#     count = 0
#     for i in num:
#         if i == 0:
#             count += 1
#         elif count == 1:
#             result.append(i)
#     print(result)
# between([1,2,0,3,4,5,6,7,8,0])


## 2.
# numbers = [1, 2, 3, 4, 5, 6]

# assume first two numbers
# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print(second_largest)


# largest = numbers[0]
# second_largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print(second_largest)

#  Unique Elements in Order
# Remove duplicates but maintain the original order.
# Example:
# Input: [1,2,2,4,3,1,2,4]
# Output: [1,2,3,4]


# number = [3,1,2,3,2,3,4,5,5,6]
# result = []
# for i in number:
#     if i not in result:
#         result.append(i)
# print(result)



# ✅ NEW DIFFICULT & LOGICAL QUESTIONS
# 1️⃣ Replace elements at even index with their square (0th, 2nd, 4th...)

# Input:
# [3, 2, 5, 4, 6, 7]

# Output:
# [9, 2, 25, 4, 36, 7]

###
def is_replace(num):
    result = []
    for i in range(0,len(num),+1):
        if i % 2 == 0:
            square = num[i] * num[i]
            result.append(square)
        else:
            result.append(num[i])

    print(result)


is_replace([2,1,3,4,5,7,9])


# def query(a):
#     b = ""
#     c =  ""
#     d = ""
#     for i in range(2,len(a)-2):
#         b = a[i] + b
#     for i in range(0,2):
#         c +=a[i]
#     for i in range(len(a)-2,len(a)):
#         d +=a[i]
#     print(c+b+d)
# query("Success")


# def is_split(num):
#     # num = words[0]
#     words = num.split()
#     num = words[0]
#     for i in words:
#         if len(i) > len(num):
#             num = i
#     print(num)


def is_splitting(num):
    words = num.split()
    smallest = words[0]
    for w in num:
        if len(words) < len(smallest):
            smallest = w
    print(smallest)
is_splitting("python is more powerful")




       