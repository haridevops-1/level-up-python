# 1.Print characters that are uppercase
# Question:
#  Given a string, print only the uppercase characters.
#  Input: "HeLLoWorld"
#  Output: H L L W


def is_uppercase(word):
    if len(word) == 0:
        print("Invalid Input")
    else:
        result = ""
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(0,len(word),+1):
            # print(word[i])
            if word[i] in upper:
                result = result + word[i]
        print(result)
is_uppercase("HeLLoWorld")
            
