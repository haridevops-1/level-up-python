# Question 2 — Create a List of First and Last Characters

# Given a list of words, make a new list containing each word’s first and last character.
# Use one loop.

# Sample Input: ["cat", "apple", "sun"]
# Sample Output: ['ct', 'ae', 'sn']


def is_concat_first_and_last_ch(word):
    if len(word) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in range(len(word)):
            first_char = word[i][0]        # first character
            last_char = word[i][len(word[i])-1]  # last character (manual, no slicing)
            result.append(first_char + last_char)  # combine
        print(result)

        
is_concat_first_and_last_ch(["cat", "apple", "sun"])
            