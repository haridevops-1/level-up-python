# Q4. Count Digits in a String

# Given a string, count how many characters in it are digits.
# Use one loop to check each character.
# Sample Input: a1b23c456
# Sample Output: 6   

def is_count_integers_only(words):
    if len(words) == 0:
        print("Invalid Input")
    else:
        integers = "0123456789"
        count = 0
        for el in range(0,len(words),+1):
            # print(words[el])
            if words[el] in integers:
                count =count +1
        print("Total integers count is:", count)
is_count_integers_only("a1b23c456")