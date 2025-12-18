# 3. Write a python program to find the words that has more than 4 characters
# Sample Input:
# This is a python program
# Sample Output:
# python
# program

def more_than_fourletters(sentence):
    if len(sentence) == 0:
        print("Invalid Input")
    else:
        words = sentence.split()
        # print(words)
        for ch in words:
            if len(ch) > 4:
                print(ch)
           
            
more_than_fourletters("This is a python program")