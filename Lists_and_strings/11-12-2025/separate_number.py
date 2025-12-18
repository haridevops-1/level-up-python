# 9️⃣ Question 9 – Separate even and odd numbers from a list

# Write a Python program that places even numbers in one list and odd numbers in another.
# Print both lists.

# Sample Input:
# [12, 7, 5, 20, 9]

# Sample Output:
# Even → [12, 20]
# Odd → [7, 5, 9]

def separate_number(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        even = []
        odd = []
        for el in range(0,len(num),+1):
            if num[el] % 2 ==0:
                even.append(num[el])
            else:
                odd.append(num[el])
        print("Even ->", even)
        print("Odd ->", odd)
    
    
(separate_number([12,7,5,20,9]))