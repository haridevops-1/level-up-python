# Level3 :
# 1.Write a Python program that splits a sentence into words and finds the longest word in it.
# Sample Input:

# Data science evolves every year
# Sample Output:

def longest_word(word):
    if len(word) == 0:
        print("Invalid Input")
    else:
        result = word.split()
        # print(result)
        max_len = ""
        for el in result:
            if len(el) > len(max_len):
                max_len = el
        print(max_len)
        


longest_word("Data science evolves every year")