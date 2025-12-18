# - Given two equal-length arrays maths and science,
#   return the indexes of students who scored > 80 in both subjects.

# Input:
# maths [92, 45, 81], science [88, 90, 70]

# Output: [0]

def is_checking(maths, science):
        result = []
        for ch in range(0,len(maths),+1):

            if maths[ch] >80 and science[ch] > 80:
                result.append(ch)
                # print(ch)
        print(result)

is_checking([92,45,81], [88,90,70])