# Filter Numbers Less Than a Target

# Description:
# You are given a list of integers and a value target.
# Create a new list that contains only the numbers strictly less than target.
# Use a single loop and compare each number with target.

# Testcase 1
# Input: nums = [5, 2, 8, 1, 10], target = 5
# Output: [2, 1]

# Testcase 2
# Input: nums = [7, 9, 11], target = 7
# Output: []

def is_filter_numbers(num,target):
    if len(num) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in num:
            if i < target:
                result.append(i)
        print(result)
is_filter_numbers([5, 2, 8, 1, 10], target = 5)
is_filter_numbers([7, 9, 11], target = 7)