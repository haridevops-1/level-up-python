# Write a program to count characters that match at the same index in two strings.
# Input: "abcde", "abzde"
# Output: 4

def count_matchwords(text: str, match: str):
    if len(text) == 0:
        return "Invalid Input"
    else:
        count = 0
        for ch in range(0,len(text),+1):
            if text[ch] in match:
                count = count + 1
        return count
print(count_matchwords("abcde", "abzde"))    