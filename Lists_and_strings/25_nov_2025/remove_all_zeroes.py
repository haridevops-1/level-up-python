# Remove All Zeros (Keep Non-Zero Only)

# Description:
# You are given a list of integers that may contain zeros.
# Create a new list that contains all the elements except the zeros.
# Use a single loop to skip zeros and keep only the non-zero values.

# Testcase 1
# Input: nums = [0, 5, 0, 3, 0, 9]
# Output: [5, 3, 9]

# Testcase 2
# Input: nums = [0, 0, 0]
# Output: []


def is_remove_zeroes(num):
    if len(num) ==0:
        print("something went wrong")
    else:
        result = []
        for i in range(0,len(num),+1):
            if num[i] != 0:
                result.append(num[i])
        print(result)
is_remove_zeroes( [0, 5, 0, 3, 0, 9])
is_remove_zeroes([0, 0, 0])
