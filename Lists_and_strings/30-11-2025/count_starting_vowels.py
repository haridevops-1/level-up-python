# Question 1 — Count Words Starting With a Vowel

# Write a program that takes a list of words and counts how many start with a vowel.
# Use one loop to check each word.
# Print the final count.

# Sample Input:
# ["apple", "cat", "orange", "ice", "banana"]

# Sample Output:
# Words starting with a vowel: 3

def is_count_starting_vowels(num):
    if len(num) == 0:
        print("Invalid Input")
    else:
        count = 0
        vowels = "aeiou"
        for i in range(0,len(num),+1):
            if num[i][0] in vowels:
                count = count + 1
        print("Words starting with a vowel:", count)


is_count_starting_vowels( ["apple", "cat", "orange", "ice", "banana"])