# a = [1,2,3,4,5,6,7,8,9,10]
# b = [10,20,30,40,50,60,70]
# print(a [1])
# print(a [-1])

# a.append(11)
# print(a)

# a.append(b)
# print(a)

# a.insert(10, 200)
# print(a)

# a.pop(10)

# a.pop()
# print(a)

# a.extend(b)
# print(a)

######### tuple
# a = (10,20,30,40)
# b = list(a)
# print (b)

# b.append(10)
# print(b)

# c = tuple(b)
# print(type(c))


# Reverse the order of words in a sentence

# word = "Python is my favourite"
# for i in range (-1, (len(word))-1, -1):
#     print(word)


# print("hello world"[::-1])
# result = ""
# for i in range (len(word)-1, -1, -1):
#     # result +=i
#     print(i)



# numbers = [1, 2, 3, 2, 4, 1]
# result = []
# duplicate = []


# for num in numbers:
#     if num not in result:
#         result.append(num)
#     elif num not in duplicate:
#         duplicate.append(num)
# print(result)
# print(duplicate)
    

# numbers = [1, 2, 3, 2, 4, 1]
# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i])

    # Write a program to find the sum and average of all numbers in a list

# numbers = [10,20,30,405]
# sum = 0
# for i in range(0, len(numbers), +1):
#     sum += numbers[i]
# print(sum)
# average = sum / len(numbers)
# print(average, sum)

#Find the largest and smallest elements in a list without using max() or min()

numbers  = [102,8049,7373,49]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i


print(largest)
print(smallest)
