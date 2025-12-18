
def is_counting(word1, word2):
    count = 0 
    if len(word1) == len(word2):
        for i in range(0,len(word1)):
            if word1[i] not in word2[i]:
                count += 1
        if count <= 1:
            print("Yes")
        else:
            print("no")
    else:
        print("Invalid")

is_counting("coding", "coting")
is_counting("coding", "coti")


