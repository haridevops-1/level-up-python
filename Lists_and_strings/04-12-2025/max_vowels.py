# 2. Write a Python program to find the word that has maximum number of vowels from the given sentence
# Sample Input:
# Learning Python is interesting
# Sample Output: interesting

def max_vowels(text: str):
    if len(text) == 0:
        print("Invalid Input")
    else:
        words = text.split()
        # count = 0
        vowels = "aeiou"
        maxi = []
        for el in words:
            count = 0
            # print(el)
            for j in el:
                # print(j)
                if j in vowels:
                    count =count + 1
            maxi.append(count)
            print(maxi)
        f = maxi[0]
        for i in range(len(maxi)):
            if maxi[i] > f:
                f = maxi[i]
        print(words[i])
            
            
            
            
            
max_vowels("Learning Python is interesting")