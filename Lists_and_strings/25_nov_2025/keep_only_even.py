# Keep Only Even Numbers

# Description:
# Given a list of integers, create a new list that contains only the even numbers.
# You must use a single loop to go through the list and decide which numbers to keep.
# Ignore all odd numbers.

# Testcase 1
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]

# Testcase 2
# Input: nums = [11, 21, 32, 44, 55]
# Output: [32, 44]

def is_only_even(num):
    if len(num) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in range(0,len(num),+1):
            if num[i] % 2 == 0:
                result.append(num[i])
        print(result)
is_only_even([11, 21, 32, 44, 55])
is_only_even([1, 2, 3, 4, 5, 6])