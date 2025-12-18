# - Write a Program that Keep Words That Start and End With the Same Letter

# ```python
# Case-insensitive matching.
# Example:
#  Input: ["level", "Apple", "mana", "cool"]
#  Output: ["level"]
# ```

def is_case_sensitive(words):
    if len(words) == 0:
        print("Invalid Input")
    else:
        result = []
        for word in words:
            # Convert first and last char to lowercase
            first = word[0].lower()
            last = word[-1].lower()

            if first == last:
                result.append(word)

        print(result)

is_case_sensitive(["level", "Apple", "mana", "cool"])