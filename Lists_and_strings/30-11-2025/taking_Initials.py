# Question 4 — Build Initials From Names

# Take a list of full names and extract the first letter of each name using one loop.
# Combine the initials into one string.
# Print the resulting initials.

# Sample Input:
# ["Alice", "Bob", "Charlie"]

# Sample Output:
# ABC

def is_taking_Initials(word:list[str]):
    if len(word) == 0:
        print("something went wrong")
    else:
        result = ""
        for ch in range(0,len(word),+1):
            result = result + word[ch][0]
        print(result)
        
is_taking_Initials( ["Alice", "Bob", "Charlie"])