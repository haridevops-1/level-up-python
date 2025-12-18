# # Question -1

# Take a number and check if it’s a multiple of 5 or not.

# def is_multiple (num):
#     if num % 5 == 0:
#        print ("It is multiple:", num)
#     else:
#         print("Not Multiple:", num)

# is_multiple(25)
# is_multiple(31)

# question -2

# Find the greatest among three numbers entered by the user.


# def is_among_biggest(a,b,c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)

# is_among_biggest(10,20,30)
# is_among_biggest(10,60,30)

#question -3

# A company gives 10% bonus if salary ≥50000, else 5%. Find total salary.

# def is_salary(money):
#     if money >= 50000:
#        total = money * 0.10
#        result = money + total
#        print(result)
#     else:
#         total = money * 0.05
#         result = money * total
#         print(result)
# is_salary(60000)
# is_salary(15000)

# question -4

# For a given number n, print whether it’s positive, negative, or zero.

# def is_number(num):
#     if num > 0:
#         print("It is positive:", num)
#     else:
#          print("It is Negative:", num)

# is_number(12)
# is_number(-90)

#Question -5

#  Input a number.If it’s divisible by both 3 and 5 → print “FizzBuzz” If only by 3 → print “Fizz”
#  If only by 5 → print “Buzz”
#  Else print “None”

# def is_number(var):
#     if var % 3 == 0 and var % 5 ==0:
#         print("FizzBuzz:", var)
#     elif var % 3 == 0:
#         print("Fizz:", var)
#     elif var % 5 == 0:
#         print("Buzz:", var)

# is_number(30)
# is_number(33)

#Question -6

#  Input a year and check if it’s a leap year or not.
#  Output: “Leap Year” or “Not a Leap Year”

# def is_year_checking(num):
#     if num % 4 == 0 :
#         print("It's Leap year:", num)
#     else:
#         print("It's Not leap Year:", num)

# is_year_checking(2005)
# is_year_checking(2004)
# is_year_checking(2000)

# question -7

#  Take user input for marks.If marks ≥ 90 → Grade A. If marks ≥ 75 → Grade B. 
# If marks ≥ 60 → Grade C. Else → Fail

# def is_student_marks(mark):
#     if mark >= 90:
#         print("Grade A:", mark)
#     elif mark >= 75:
#         print("Grade B:", mark)
#     elif mark >= 60:
#         print("Grade C:", mark)
#     else:
#         print("Fail:", mark)

# is_student_marks(56)
# is_student_marks(80)

#question -8

#  Input a character.
#  If it’s a vowel (a, e, i, o, u), print “Vowel”, else print “Consonant”.

# def is_character(v):
#     if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
#         print("It is a vowel", v)
#     else:
#         print("It is consonant", v)

# is_character(e)

#Question -9

#  A student has to attend 75% classes to write exams.
#  Input: Total classes, Attended classes.
#  If attendance ≥ 75% → print “Allowed”
#  Else → print “Not Allowed”

# def is_exam(Total_classes, Attended_classes):
#     if Attended_classes >= 75:
#         print("you're Allowed")
#     else:
#         print("You're not allowed")

# is_exam(100, 76)
# is_exam(100, 45)

#Question -10

# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print("Factorial of", num, "is:", fact)

# factorial(5)
# factorial(10)