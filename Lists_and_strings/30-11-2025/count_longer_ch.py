# Question 3 — Count Characters Longer Than 3 Letters

# Write a program that takes a list of strings and counts how many have more than 3 characters.
# Do this using only one loop.
# Print the count.

# Sample Input:
# ["hi", "hello", "car", "python", "go"]

# Sample Output:
# Strings longer than 3 characters: 2

def is_count_longer_ch(word: list[str]):
    if len(word)== 0:
        print("Invalid")
    else:
        result = []
        count = 0
        for ch in range(0,len(word),+1):
            # print(word[ch])
            if len(word[ch]) > 3:
                count = count +1
        print( "Strings longer than 3 characters:", count)
               
is_count_longer_ch(["hi", "hello", "car", "python", "go"])