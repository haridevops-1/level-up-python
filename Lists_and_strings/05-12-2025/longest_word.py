# 10. find_longest_word(words)

# Return the longest word in a list of strings.
# If tie → return the first longest.

# Input:
# ["cat", "elephant", "dog", "hippo"]
# Output:
# "elephant"

def longest_word(sentence: list[int]):
    if len(sentence) ==0:
        print("Invalid Input")
    else:
        max_len = ""
        for ch in sentence:
            # print(ch)
            if len(ch) > len(max_len):
                max_len = ch
        print(max_len)
            
longest_word(["cat", "elephant", "dog", "hippo"])