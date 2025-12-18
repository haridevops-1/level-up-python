# 7. remove_value(arr, value)

# Remove all occurrences of a value from the array (no remove(), no filter()).

# Input:
# [3, 1, 3, 5, 3], 3
# Output:
# [1, 5]

def remove_value(arr: list[int], value: int):
    if len(arr) == 0:
        print("Invalid Input")
    else:
        result = []
        for el in range(0,len(arr),+1):
            if value != arr[el]:
                result.append(arr[el])
        print(result)
remove_value( [3, 1, 3, 5, 3], 3)