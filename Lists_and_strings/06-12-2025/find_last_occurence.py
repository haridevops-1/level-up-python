# # 1️⃣ Find Last Occurrence

# # Write a function that returns the last index of a given value in a list.
# # If the value doesn't exist, return -1.
# # Input: [3, 5, 2, 5, 1], value = 5
# # Output: 3


def find_last_occurence(num: list[int], value: int):
    if len(num) == 0:
        print(-1)
    else:
        last_index= -1
        for i in range(len(num)):
            if num[i] == value:
                last_index = i
        return last_index
    
print(find_last_occurence( [3, 5, 2, 5, 1], 5))    

    