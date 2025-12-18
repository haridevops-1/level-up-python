# 6️⃣ Check If List Sorted

# Return True if the list is sorted in ascending order.
# Input: [1, 2, 3, 5, 4]
# Output: False

def ascending_order(num: list[int]):
    if len(num) == 0:
        print("Invalid Input")
    else:
        for i in range(len(num)):
            if num[i] > num[i+1]:
                return False
        return True
    
print(ascending_order( [1, 2, 3, 5, 4]))