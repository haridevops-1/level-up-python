# Q5. Find Total Digits in a String

# Write a program to count how many digits are present in a string.
# Input: "a1b2c3"
# Output: 3

def Total_digits(text: str):
    if len(text) == 0:
        return "Invalid Input"
    else:
        count = 0
        numbers = "1234567890"
        for ch in range(0,len(text),+1):
            if text[ch] in numbers:
                count = count + 1
        return count
        
print(Total_digits("a1b2c3"))
