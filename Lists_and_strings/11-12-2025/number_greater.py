# Peak = number which is greater than neighbours.
#  Return any peak index.
# Example:
#  Input: [1,2,1,3,5,6,4]
#  Output: 1 or 5


def number_greater(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        result = []
        for i in range(0,len(num),+1):
                for j in range(0,len(num),+1):
                     if num[i] > num[j]:
                        result.append(i)
    print(result)

number_greater([1,2,1,3,5,6,4])

