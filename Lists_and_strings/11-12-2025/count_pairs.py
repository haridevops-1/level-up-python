# # Count pairs where the second number is bigger
# Test case 1:
# Input

# [1, 5, 2, 6, 3, 9]
# Output

# 3


def count_pairs(num:list[int]):
    if len(num)== 0:
        print("Invalid Input")
    else:
        even = []
        odd = []
        for i in range(0,len(num),+1):
            if i % 2 == 0:
                even.append(num[i])
            else:
                odd.append(num[i])
        # print(odd)
        # print(even)
        count = 0
        for i in range(0,len(odd),+1):
            if odd[i] > even[i]:
                count += 1
        print(count)
            
count_pairs([1,5,2,6,3,1])