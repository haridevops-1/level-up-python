# Q9. Count Words With Length Between Two Values (10 marks)

# Write a function that returns how many words have lengths between min_len and max_len.
# Input: ["hi", "hello", "python", "go"], min=2, max=4
# Output: 2

def count_words_length(word: list[int]):
    if len(word) == 0:
        return "Invalid Input"
    else:
        count = 0
        for ch in range(0,len(word),+1):
            if len(word) == min and max:
                count += 1
        return count




print(count_words_length( ["hi", "hello", "python", "go"], min=2, max=4))