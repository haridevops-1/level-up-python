# Return the sum of all indices where the value is even.

# Input:
# [5, 2, 7, 8, 10]
# Even numbers: 2 (index 1), 8 (index 3), 10 (index 4)

# Output:
# 1 + 3 + 4 = 8

def sum_of_indices(num: list[int]):
    if len(num) ==0:
        print("Invalid Input")
    else:
        sum = 0
        for el in range(0,len(num),+1):
            if num[el] % 2 == 0:
                sum = sum + el
        print(sum)
        
sum_of_indices([5, 2, 7, 8, 10])
sum_of_indices([5, 1, 7, 8, 11])
                