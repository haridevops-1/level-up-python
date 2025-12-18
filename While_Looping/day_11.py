
#  Question 1: Temperature Check

# If temp > 30 → print “Hot Day”
#  If temp between 20–30 → print “Normal Day”
#  Else → print “Cold Day”

# def is_temperature_check(temp):
#     if temp > 30:
#         print("It's Hot day:", temp)
#     elif temp >= 20 and temp <= 30:
#         print("It's normal day:", temp)
#     else:
#         print("It's cold day:", temp)

# is_temperature_check(24)
# is_temperature_check(12)


# Question 2: Percentage Bonus

# A student gets a scholarship:
# If marks ≥ 90 → bonus ₹2000
# If marks ≥ 75 → bonus ₹1000
# Else → no bonus
#  Calculate total money if base scholarship is ₹5000.

# base_scholarship = 5000

# ## start
# marks = int(input("Enter your marks:"))

# if marks >= 90:
#     bonus = 2000
# elif marks >= 75:
#     bonus = 1000
# else:
#     bonus = 0

# ## stop

# total_salary = base_scholarship + bonus
# print(total_salary)

# Question -3: Student scholarship logic:
#  If marks ≥ 90 → 50% fee discount
#  If marks ≥ 80 → 25% discount
#  Else → no discount
#  Input marks and fee, print final fee after discount.

# Question -4: def is_scholarship(marks, fee):
#     # fees = 90000

#     if marks >= 90:
#         discount = fee * 0.50
#     elif marks >= 80:
#         discount = fee * 0.25
#     else:
#         discount = fee
#     print(fee)

# is_scholarship(92, 90000)
# is_scholarship(82, 80000)

# Question -5: Input 10 integers and count how many are positive, negative, and zero.

def is_count(num):
    count = 0
    if num > 0:
        count += 1
        print(count)
    elif num < 0:
        count= +1
        print(count)
    elif num == 0:
        count =+1
        print(count)
    else:
        print("Invalid Input")
    
is_count(123)





