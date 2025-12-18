    # Filter numbers satisfying 3 conditions
#   Problem:
#   Print numbers that:

# 1. are 4 digits
# 2. end with an even digit

# Input: [2481, 3572, 602, 7890, 4214]
# Expected Output: [3572,7890 ,4214]
# ```


def is_even(num):
     result = []
     for i in range(0,len(num),+1):
          if num[i] % 2 == 0 and num[i] > 1000 and num[i] < 9999:
               result.append(num[i])
     print(result)
is_even([2481, 3572, 602, 7890, 4214])