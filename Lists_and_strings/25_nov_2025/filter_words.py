# Filter Words Starting With a Given Letter

# Description:
# You are given a list of words and a character ch.
# Create a new list containing only the words that start with the character ch
# (case-sensitive). Use a single loop.

# Testcase 1
# Input: words = ["apple", "ant", "ball", "arrow"], ch = 'a'
# Output: ["apple", "ant", "arrow"]

# Testcase 2
# Input: words = ["Cat", "car", "dog"], ch = 'c'
# Output: ["car"]
# (Only "car" starts with lowercase 'c'; "Cat" starts with 'C'.)

def is_filter(word,ch):
    if len(word) == 0 or len(ch) == 0:
        print("Invalid Input")
    else:
        result= []
        for i in range(0,len(word),+1):
            for j in word[i]:
                if j[0] == ch:
                    result.append(word[i])
        print(result)


is_filter(["Cat", "car", "dog"],'c') 
