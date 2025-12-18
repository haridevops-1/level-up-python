# ✅ 1. Count how many times a character appears in a string

# Question:
# Write a program to count how many times the character 'a' appears in a given string.

# Input: "banana"
# Output: 3

def count_array(text: str):
    if len(text) == 0:
        print("Invalid Input")
    else:
        count = 0
        for el in text:
            # print(el)
            if el == "a":
                count += 1
        return "Total count of a is:", count
            
print(count_array("banana"))