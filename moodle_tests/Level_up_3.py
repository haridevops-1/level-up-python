def min_max_diff(nums):
    #finding the max 
    max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
    
    #find min
    
    min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min:
            min = nums[i]
    
    print (max - min)

min_max_diff([10,9,8,1,8])

def compare_print_g_b(s, t):
    result = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            result += "G"
        else:
            result += "B"
    print(result)
  
compare_print_g_b("APPLE", "APRON") 


def compare_print_g_b(a,b):
    output = ""
    for i in range(0, len(a)):
        if a[i] == b[i]:
            output += "S"
        else:
            output += "G"
    print(output)
compare_print_g_b("HELLO", "HEART")
