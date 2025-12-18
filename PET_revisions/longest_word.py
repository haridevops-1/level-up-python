# Question 2: Find the Longest Word in a Sentence
# Problem Statement
# You are given a sentence consisting of multiple words separated by spaces.
#  Write a Python program to find and print the longest word in the sentence.
# If two or more words have the same maximum length, print the first occurring word.
# Input
# A single line string representing a sentence.
# Output
# The longest word in the sentence.
# Sample Input

# Python programming is very interesting
# Sample Output

# programming
# Explanation
# Word lengths:
# Python → 6
# programming → 11
# is → 2
# very → 4
# interesting → 11
# programming appears first among the longest words.

def longest_word(sentence: str):
    if len(sentence) == 0:
        return "Invalid Input"
    else:
        words = sentence.split(" ")
        max_length = words[0]
        for ch in words:
            if len(ch) > len(max_length):
                max_length = ch
        return max_length
print(longest_word( "Python programming is very interesting"))