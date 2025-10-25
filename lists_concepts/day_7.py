# numbers = [1,2,3,4,5,6,7,8,9,]
# numbers.remove(2)
# print(numbers)

# numbers = [10,20,30,40,50,60,70]
# numbers.append (80)
# print(numbers)

# numbers = [1,2,3,4,5,6,7]
# numbers.insert(5, 90)
# # print(numbers)

# nadhiya = [10,20,30,40,50,60]
# nadhiya.pop()
# print(nadhiya)

# Sum of All Numbers

# Write a Python program to find the sum of all numbers in a list.
# Example:
# Input → [5, 10, 15, 20]
# Output → 50

def sum_of_numbers (n):
    sum = 0
    for i in n:
        sum = sum + i
    print(sum)
sum_of_numbers([10,15,20,25])

# 2. Extend a List

# Combine these two lists using .extend():
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Output → [1, 2, 3, 4, 5, 6]

# a = [1,2,3,4]
# b = [5,6,7,8]
# a.extend(b)
# print(a)

#3. Add a new fruit 'mango' to the end of the list using .append().

# fruits = ['grapes', 'orange', 'apple']
# fruits.insert(3, 'mango')
# print(fruits)

#4. Insert 'orange' at index 2 in your fruit list.

# fruits = ['butterfruit', 'pineapple', 'mango', 'pomegranate']
# fruits.insert(2, 'orange')
# print(fruits)

# 5.Combine two lists list1 = [1, 2, 3] and list2 = [4, 5] using .extend().

# a_list = [1,2,3,4,5,6]
# b_list = [7,8,9,10]
# a_list.extend(b_list)
# print(a_list)

# 6. remove 'banana' from the fruit list.

# fruits = ['butterfruit', 'banana', 'pineapple', 'mango', 'pomegranate']
# fruits.remove('mango')
# print(fruits)

# 7. Print the first and last elements of a list of numbers [10, 20, 30, 40, 50].

# new_list = [10,20,30,40,50,60]
# print(new_list[0:4])

#8. Replace the third element of [5, 10, 15, 20] with 50.

# numbers = [5,10,15,20,25]
# numbers [2]= 50
# print(numbers)

#9. Find the sum of [2, 4, 6, 8, 10].

# input_list = [2,4,6,8,10]
# total = 0
# for i in input_list:
#     total+=i
# print(total)

#10. Find the maximum and minimum numbers in [12, 45, 7, 23, 89].

# def is_max_numbers(num):
#     print(max(num))
# is_max_numbers([12,30,90])
# is_max_numbers([100,200,500])

#11. Count how many times 2 appears in [1, 2, 2, 3, 2, 4].


# 12. Reverse the list [1, 2, 3, 4, 5] without using .reverse().

# def is_reverse (num):
#     for i in num[::-1]:
#         print(i)
# is_reverse([1,2,3,4,5])        

# 13. Print only the even numbers from [1, 2, 3, 4, 5, 6].

# def is_even_numbers(num):
#     for i in num:
#         if i % 2 == 0:
#             print(i)
# is_even_numbers([2,3,4,5,6,7,8,9,10])

# 14. Copy a list [10, 20, 30] into a new list using .copy().

# new_list = [10,20,30]
# copied_list = new_list.copy()
# print(copied_list)


# 15. Add numbers 1 to 5 to an empty list using a for loop and .append().

# 16. Insert 'Python' at the beginning of ['Java', 'C++', 'Ruby'].

# input = ['java', 'c++', 'Ruby']
# input.insert(0, 'Python')
# print(input)

# 17.Merge ['a', 'b'] and [1, 2, 3] into a single list.

# input_1 = ['a', 'b']
# input_2 = [1,2,3]
# print(input_1 + input_2)

#18. Remove the last element of [10, 20, 30, 40].

input = [10,20,30,40]
input.remove(input[3])
print(input)

# 19. Find the length of ['apple', 'banana', 'cherry', 'date'].
# length = ['apple', 'banana','orange', 'Grapes']
# print(len(length))     

#20. Replace 'Math' with 'Computer' in ['Math', 'Science', 'English'].
# input = ['Math', 'science', 'English']
# input[0] = 'Computer science'
# print(input)

# 21. Add a list [7, 8, 9] as a single element to [1, 2, 3] using .append().
# numbers = [1,2,3,4]
# extra = [5,6,7,8]
# numbers.extend(extra)
# print(numbers)        