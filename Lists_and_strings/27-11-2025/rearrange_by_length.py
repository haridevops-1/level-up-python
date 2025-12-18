# Rearrange by Length
# Given a list of words, rearrange them so shorter words come first.
#  (Don't use sort() or sorted())
# Input:
#  ["banana", "cat", "watermelon", "apple"]
# Output:
#  ["cat", "apple", "banana", "watermelon"]


def rearrange_by_length(text):
    if len(text) == 0:
        print("Invalid Input")
    else:
        max = 0
        output = []
        for i in text:
            # print(len(i))
            result = len(i)
            print(result)
            if result > max:
                output.append(text)
                max = result
            print(output)

        
            
   


rearrange_by_length(["banana", "cat", "watermelon", "apple"])