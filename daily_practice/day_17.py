# 1. Check whether the given character is a vowel or not
# Note: Given Character is in lowercase

def is_vowel(value):
    vowels = 'aeiou'
    if value in vowels:
        print("It's a vowel")
    else:
        print("Not a vowel")

# Test
is_vowel("a")   # It's a vowel
is_vowel("b")   # Not a vowel

# 2. Let "A" be a year, write a program to check whether this year is a leap year or not.

# def is_leap_year(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print("Y")
#     else:
#         print("N")

# # Test
# is_leap_year(2020)  # Y
# is_leap_year(2023)  # N


# Print "Y" if it's a leap year and "N" if it's a common year.


# Input Description:
# A Year is the input in the form of a positive integer.

# Output Description:
# Print "Y" if it's a leap year and "N" if its a common year.

# Sample Input :
# 2020
# Sample Output :
# Y


# 3. Write a function print_characters(charc, n) which prints the number of characters n times. 
# Example: print_characters('*', 5), prints the output as * * * * *

def print_characters(charc, n):
    for i in range(n):
        print(charc, end=' ')
    print()  # for new line

# Test
print_characters('*', 5)  # * * * * *
