# Q7. Replace All Vowels in a String with '*' (10 marks)

# Write a function that replaces every vowel in a string with '*'.
# Input: "education"
# Output: "*d*c*t**n"

def replace_vowels(text: str):
    if len(text) == 0:
        return "Invalid Input"
    else:
        vowels = "aeiouAEIOU"
        result = ""
        for ch in range(0,len(text),+1):
            if text[ch] in vowels:
                result +="*"
            else:
                result += text[ch]
        return result
    
print(replace_vowels("education"))
