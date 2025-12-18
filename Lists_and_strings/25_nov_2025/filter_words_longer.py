# Filter Words Longer Than 3 Characters

# Description:
# Given a list of strings (words), create a new list containing only the words
# whose length is greater than 3.
# Use a single loop to check the length of each word and filter accordingly.

# Testcase 1
# Input: words = ["hi", "hello", "to", "code", "sun"]
# Output: ["hello", "code"]

# Testcase 2
# Input: words = ["cat", "dog", "lion", "tiger"]
# Output: ["lion", "tiger"]

def is_filter_by_longer(word):
    if len(word) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in word:
            if len(i) > 3:
                result.append(i)
        print(result)
is_filter_by_longer( ["cat", "dog", "lion", "tiger"])
        