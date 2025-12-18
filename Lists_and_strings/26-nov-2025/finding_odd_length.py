# - Given a list of strings , For Each word, Check whether the length of the element is odd and the middle letter of that word must be a vowel , print the words line by line

# ```python
# # test case 1
# Input: ["cat", "read", "room", "hello", "sky"]
# Output: cat room hello
# ```
def is_finding_length(text):
    if len(text) == 0:
        print("Invalid Input")
    else:
        result = []
        vowels= "aeiou"
        for i in text:
            if len(i) %2 != 0:
                result.append(i)
        print(result)
            # for j in i:
            #     print(j)
is_finding_length(["cat", "read", "room", "hello", "sky"])
                
            