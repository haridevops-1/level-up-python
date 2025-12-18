# Q1. Count Words Starting With Vowels

# Write a program that reads a list of words and counts how many begin with a vowel.
# Use only one loop to solve this.
# Sample Input: apple egg cat orange ink dog
# Sample Output: 4

def is_count_starting_vowels(word):
    if len(word)== 0:
        print("Invalid Input")
    else:
        count = 0
        vowels= "aeiou" or "AEIOU"
        for ch in range (0,len(word),+1):
            # print(word[ch])
            if word[ch][0] in vowels:
                count = count + 1
        print("Total starting vowels word:", count)
            
is_count_starting_vowels(["apple", "egg", "cat", "orange", "ink", "dog"])   