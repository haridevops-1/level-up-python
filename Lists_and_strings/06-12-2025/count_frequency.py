#  2️⃣ Count Frequency

# Count how many times a number appears in the list without using count().
# Input: [1, 4, 4, 2, 4], value = 4
# Output: 3

def count_frequency(num: list[int], value: int):
    if len(num) == 0:
        print("some error occured")
    else:
        count = 0
        for el in range(len(num)):
            if num[el] == value:
                count = count + 1
        return count
        
print(count_frequency([1,4,4,2,4], value = 4))