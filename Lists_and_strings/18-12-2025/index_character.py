# # Q2. Find All Indices of a Character

# # Write a program to find all positions of a given character in a string.
# # Input: "banana", character = 'a'
# # Output: [1, 3, 5]

def index_character(word: str, char: str):
    if len(word) ==0:
        return "Invalid Input"
    else:
        result = []
        for el in range(0,len(word),+1):
            if word[el] == char:
                result.append(el)
        return result 
            
print(index_character("banana", "a"))

