
# - You are given a list containing integers, floats and strings.
# Create a new list containing only the float values using one loop.
# ```python
# Example:
# Input: [10, 3.5, "hello", 8.2, 6]
# Output: [3.5, 8.2]
# ```

def is_float(value):
    if len(value)== 0:
        print("Invalid Input")
    else:
        result = []
        for i in range(0,len(value),+1):
            if type(value[i]) == float:
                result.append(value[i])
        print(result)
is_float([10,3.5,"hello",8.2,6])
