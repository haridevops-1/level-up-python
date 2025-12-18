# Given a list and a target value, return all indices where the target appears.
#  Example: [1, 2, 3, 2, 4, 2] → target 2 → indices [1, 3, 5].

def is_target_value(num, target):
        result = []
        for i in range(0,len(num)):
            if num[i] == target:
                result.append(i)
        print(result)
is_target_value( [1, 2, 3, 2, 4, 2],2)