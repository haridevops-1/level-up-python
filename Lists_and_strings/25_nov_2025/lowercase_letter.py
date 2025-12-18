# - Given a list of words, print only the ones that start with an uppercase letter.
#   Use a single loop to check their first character.

# Input: ["Apple", "ball", "Cat", "dog"]
# Output: Apple Cat

def lower_case_letters(word):
    ##start
    if len(word) == 0:
        print("Invalid Input")
    else:
        result =[]
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for ch in word:
            if ch[0] in characters:
                result.append(ch)
        print(result)

lower_case_letters(["Apple","ball","Cat", "dog"])

