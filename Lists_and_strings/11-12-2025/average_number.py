# Problem: Count How Many Numbers Are Greater Than the Average
# You are given a list:

# [4, 8, 1, 9, 3, 10, 5]

def count_number(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        sum = 0
        count_avg = 0
        for i in range(0,len(num),+1):
            sum = sum + num[i]
        average = sum / len(num)
        for el in num:
            if el > average:
                count_avg += 1
        return(count_avg)
print(count_number([4, 8, 1, 9, 3, 10, 5]))
        # print(average)