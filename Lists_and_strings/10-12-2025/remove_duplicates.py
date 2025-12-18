# Q1. Remove Duplicate Words from a List (10 marks)

# Write a function that removes duplicate words from a list while keeping the original order.
# Input: ["apple", "banana", "apple", "cherry", "banana"]
# Output: ["apple", "banana", "cherry"]


def remove_duplicates(sentence: list[str]):
    if len(sentence) == 0:
        return "Invalid Input"
    else:
        result = []
        for word in range(0,len(sentence),+1):
            if sentence[word] not in result:
                result.append(sentence[word])
        return result

print(remove_duplicates(["apple", "banana", "apple", "cherry", "banana"]))