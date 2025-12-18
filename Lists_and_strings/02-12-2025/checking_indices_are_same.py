# 2. Write a function that takes two lists of integers of the same length as input. The 
# function should count and return the number of positions (indices) where the elements 
# in both lists are exactly equal. Assume both input lists are guaranteed to have the same 
# number of elements. 
# Input: left = [1,5,2,8,3], right = [1,9,2,4,3] 
# Output : [0,2,4] 
# # here 1 and 1 matches , so first index 0 is taken 
# # 2 and 2 matches , so 2 
# # 3 and 3 at the last matches, so 4 
# # appending all the indices, we get [0,2,4]

# FUNCTION is_checking_indices(left: datatype,right: datatype):
#     CREATE an empty list called result
#     for index i in range FROM 0 to length of left_list:
#         if left_list[i] is equal to right_list[i]:
#             APPEND i index to result
#     print result 
    
def checking_indices_are_same(left_list:list[int], right_list:list[int]):
        result =[]
        if len(left_list)== len(right_list):
            for i in range(0,len(left_list)):
                if left_list[i] == right_list[i]:
                    result.append(i)
            print(result)
            
checking_indices_are_same(left_list = [1,5,2,8,3], right_list = [1,9,2,4,3] )