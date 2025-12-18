# Question 5 — Filter Out Words Containing a Specific Letter

# Given a list of words and a target letter, create a new list containing only the words without that letter.
# Use one loop to check each word.
# Print the filtered list.

# Sample Input:
# Words: ["tree", "book", "sky", "pen"]
# Letter: e

# Sample Output:
# ['book', 'sky']


def filter_without_target(text,target):
    # if len(text) or len(target) == 0:
    #     print("Invalid Input"
        result = []
        for ch in range(0,len(text),+1):
            # print(text[i])
            if target not in text[ch]:
                result.append(text[ch])
        print(result)
                
filter_without_target( ["tree", "book", "sky", "pen"],"e")
