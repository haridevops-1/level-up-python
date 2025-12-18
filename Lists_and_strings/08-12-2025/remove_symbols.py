# A website allows only lowercase letters, digits, and underscores in usernames.
# Given a username, remove all other characters.
# Input: "Ram!_Kumar@2024"
# Output: ram_kumar2024
# Input: "HELLO*123"
# Output: hello123


def remove_symbols(sentence):
    if len(sentence) ==0:
        print("Invalid Input")
    else:
        result = ""
        alpha ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        for ch in sentence:
            if ch == "_"or ch in numbers:
                result += ch 
            if ch in alpha:
                result += ch.lower()

        return result
print(remove_symbols("!Ram_kumar@2025"))