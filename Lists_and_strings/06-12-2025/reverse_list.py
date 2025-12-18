# 5️⃣ Reverse List (no reverse())

# Reverse the list using a loop and return the new list.
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]


def reverse_list(num: list[int]):
    if len(num)== 0:
        print("Invalid Input")
    else:
        reverse = []
        for el in range(len(num)-1, -1, -1):
            reverse.append(num[el])
        return reverse

print(reverse_list([1, 2, 3, 4]))
