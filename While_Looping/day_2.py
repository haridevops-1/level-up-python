# 1. Ask the user for their age — if age ≥ 18, print “You are an adult”, else print “You are a minor.”

user = int(input("Enter your age to check adult or not: "))
if user >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# 2. Ask for a number — check if it’s even or odd.

user = int(input("Enter a num to check even or odd: "))
if user % 2 == 0:
    print("It's Even")
else:
    print ("It's odd")

# 3.Ask for marks — if marks ≥ 50 print “Pass” else “Fail”.

marks = int(input("Enter your scores: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# 4. Ask for a number and print whether it’s positive, negative, or zero.

num = int(input("Enter a number to check: "))
if num > 0:
    print("positive")
else:
    print("Negative")

# 5. Ask for two numbers and print which one is larger

a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b :
    print(a)
else:
    print(b)

# 6.  Password Checker:
# Ask the user to enter a password.

user = input("Enter your password: ")
if user == "python123":
    print("Your password is correct")
else:
    print("your password is invalid")

# 7. Ask the user to enter a year.
# If the year is divisible by 4 → print “Leap Year”
# Else → print “Not a Leap Year”

user = int(input("Enter the yer to find: "))
if user % 4 == 0:
    print("It's leap year")
else:
    print("Not leap year")

# 8. Ask the user for a number.

# If divisible by 5 → print “Divisible by 5”
# Else → print “Not divisible by 5”

user = int(input("Enter the number to check:"))
if user % 5 :
    print("Divisible by 5")
else:
    print("Invalid Input")

# 9. Ask the user to enter a single character.
# If it is a vowel (a, e, i, o, u) → print “Vowel”
# Else → print “Consonant”

user = input("Enter the alphabets: ")
if user == "a" or "e" or "i" or "o" or "u":
    print("It's vowels")
else:
    print("It is consenants")

# 10. Ask the user for marks (0–100) and attendance percentage (0–100).
# If marks ≥ 50 and attendance ≥ 75 → print “Pass”
# Else → print “Fail”

marks = int(input("Enter your marks"))
attendance = int(input("Enter your attendance"))
if marks >= 50 and attendance >= 75:
    print("Pass")
else:
    print("Fail")
