# 1.Print numbers that appear more than once (duplicates only)
# Input: [1,4,2,7,4,1,8,2,2]
#  Output → 1, 2, 4

def number_appears(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        count = 0
        result = []
        for el in range(0,len(num),+1):
            for j in num:
                return j
            result.append(num[el])
            # if num[el] not in result:
            #     result.append(num[el])
        return result
            
print(number_appears([1,4,2,7,4,1,8,2,2]))