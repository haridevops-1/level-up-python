# Q7. Count Uppercase Letters in a String

# Write a program to count uppercase letters in a string.
# Input: "PyTHon"
# Output: 3

def countUpper(words: str):
    ## start
    if len(words) == 0:
        return "Invalid Input"
    else:
        count = 0
        upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        for ch in range(0,len(words),+1):
            if words[ch] in upper:
                count = count + 1
        return count 
    ##End
print(countUpper("PyTHon"))