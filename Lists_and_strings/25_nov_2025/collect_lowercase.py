### Strings

# - From a string, collect all the lowercase letters in the same order.
#   Use a single loop to scan the string.

# ```python
# # test case 1
# Input: "PyTHonProGRam"
# Output: "yonroam"
# ```

def is_lowercase(text):
    if len(text) == 0:
        print("Invalid Input")
    else:
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        for i in range(0,len(text),+1):
            if text[i] not in characters:
                result = result + text[i]
        print(result)

is_lowercase("PyTHonProGRam")