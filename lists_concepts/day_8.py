# 1.Create a list with the words from this sentence:
# "Python makes coding fun" and print the list.
# result = []
# result.append("python makes coding fun")
# print (result)

# 2. Given a list of words ['I', 'love', 'Python'], join them into a single sentence with spaces.
# value = ['I', 'love', 'Python']
# sentence = ' '.join(value)
# print(sentence)

# 3. Split the sentence "Learning Python is easy" into a list of words.
# sentence = "Learning Python is easy"
# words = sentence.split()
# print(words)


# 4. Given a list ['Python', 'is', 'awesome'], replace 'awesome' with 'powerful'.

# words = ['Python', 'is', 'awesome']
# words [2] = 'powerful'
# print(words)

# Take a sentence from the user and count how many words it has (use .split() and len()).

#6. From the sentence "Python is a popular programming language",
# print only the words that have more than 5 letters.

# 7.Convert all words in the list ['Hello', 'World', 'Python'] to lowercase.
words = ['Hello', 'World', 'Python']
lower_words = []

for word in words:
    lower_words.append(word.lower())

print(lower_words)

# 8. Given a list ['apple', 'banana', 'cherry', 'apple'],
# count how many times 'apple' appears in the list.

fruits = ['apple', 'banana', 'cherry', 'apple']
apple_count = fruits.count('apple')
print(apple_count)

# Reverse the order of words in the sentence "I am learning Python"
# (output: "Python learning am I").
value = "I am learning Python"
for i in range (0, len(value), -1):
    print(value[i])

# 10. Combine two lists of words:
# ['Coding', 'is'] and ['fun', 'and', 'creative']
# to form one complete sentence list.''
# a = ['Coding', 'is']
# b = ['fun', 'and', 'creative']
# result = a+b
# print(result)