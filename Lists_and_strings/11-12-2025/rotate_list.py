# Rotate a list to the right by 1 step (no slicing)
# Input: [1,2,3,4,5]
#  Output: [5,1,2,3,4]

# def rotate_list(num: list[int]):
#     if len(num) == 0:
#         print("Invalid Input")
#     else:
#         result = []
#         for el in range(-1, len(num)-1, +1):
#             result.append(num[el])
#         print(result)

# rotate_list([1,2,3,4,5])

## SECOND

def rotate_list(num):
    result = num[-1]
    result.append(num[0:len(num)-1])
    print(result)

rotate_list([1,2,3,4,5])