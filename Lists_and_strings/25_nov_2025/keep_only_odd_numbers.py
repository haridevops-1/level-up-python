# Keep Only Odd Numbers

# Description:
# Given a list of integers, create a new list with only the odd numbers.
# Use a single loop and keep numbers where num % 2 != 0.
# Ignore all even numbers.

# Testcase 1
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: [1, 3, 5]

# Testcase 2
# Input: nums = [10, 20, 30]
# Output: []

def is_only_odd(num):
    if len(num) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in range(0,len(num),+1):
            if num[i] % 2!= 0:
                result.append(num[i])
        print(result)


is_only_odd([1,2,3,4,5,6])
    