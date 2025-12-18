# 3️⃣ Find Smallest Number (no min())

# Loop through all values and find the smallest.
# Input: [8, 3, 6, 2, 9]
# Output: 2

def smallest_number(num: list[int]):
    if len(num) == 0:
        print("Invalid Input")
        return

    min_value = num[0]   # start with first element

    for i in range(len(num)):
        if num[i] < min_value:   # check for smaller value
            min_value = num[i]

    return min_value


print(smallest_number([8, 3, 6, 2, 9]))
