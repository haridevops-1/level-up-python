# Question 1 — Count Uppercase Letters in a List of Words

# Write a program that counts the total number of uppercase letters across all words using one loop.
# Print the total.

# Sample Input: ["Hello", "WORLD", "PyThOn"]
# Sample Output: Total uppercase letters: 9


def is_counting_upper(text):
    if len(text) == 0:
        print("Invalid Input")
    else:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = 0
        for word in text:
            for ch in range(len(word)):
                for l in range(len(upper)):
                    if word[ch] == upper[l]:
                        count = count + 1
    print("Total uppercase letters:",count)    

is_counting_upper(["Hello", "WORLD", "PyThOn"])