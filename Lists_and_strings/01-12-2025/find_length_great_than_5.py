# Q6. Count Words With More Than 5 Letters

# Write a program that reads a list of words and counts how many have more than 5 characters.
# Use only one loop to solve it.
# Sample Input: banana cat strawberry dog elephant kiwi
# Sample Output: 3
            
def is_more_than_5(text: list[str]):
    if len(text) == 0:
        print("Invalid Input")
    else:
        count = 0
        for w in text:
            # print(text[ch])
            if len(w) > 5:
                count= count + 1
            
        print(count)
            
is_more_than_5( ["banana", "cat", "strawberry", "dog", "elephant", "kiwi"])