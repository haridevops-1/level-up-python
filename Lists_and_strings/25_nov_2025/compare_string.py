s1 = "ABCDE"
s2 = "CDEAB"

'''
ABCDE
BCDEA
CDEAB
DEABC
EABCD
'''

def compare_strings(left,right):
    #start
    if len(left) == 0 or len(right) == 0:
        print("Invalid input")
    else:
        final = left
        output = False
        for i in range(0,len(left),+1):
            temp = final[1:] + final[0]
            final = temp
            if final == right:
                output = True
        print(output)
    #stop

compare_strings("ABCDE","CDEAB")
