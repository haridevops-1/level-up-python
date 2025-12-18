# Question 1: Remove Duplicates from a String
# Problem Statement
# You are given a string that may contain repeated characters.
#  Write a Python program to remove all duplicate characters from the string and return a new string that contains only the first occurrence of each character, while preserving the original order.
# Input
# A single string s containing letters, digits, or symbols.
# Output
# A string with duplicate characters removed.
# Sample Input

# programming
# Sample Output

# progamin
# Explanation
# The characters r, g, and m appear more than once.
# Only their first occurrence is kept.
# Order of characters remains the same as the input.

def remove_duplicates(text: str):
    if len(text) == 0:
        return "Invalid Input"
    else:
        result = ""
        for ch in range(0,len(text),+1):
            if text[ch] not in result:
                result += text[ch]
        return result

print(remove_duplicates("programming"))