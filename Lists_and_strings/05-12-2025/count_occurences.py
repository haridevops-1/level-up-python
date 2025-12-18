# 2. count_occurrences(arr, value)

# Count how many times a value appears in the array (no libraries).

# Input:
# [1, 2, 2, 2, 3, 4], 2
# Output:
# 3

def count_occurrences(arr: list[int], value: int):
    if len(arr) == 0:
        print("Invalid Input")
    else:
        count = 0
        for el in range(0,len(arr),+1):
            # print(el)
            if arr[el] == value:
                count = count +1
        print("Total count of value is:", count)
            
            
count_occurrences([1, 2, 2, 2, 3, 4], 2)
    