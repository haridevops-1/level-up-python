#  Write a function that merges two lists by taking elements alternately.

# ```python
# Input: x= [1, 2, 3] y= ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']


def is_merge(x,y):
    result = []
    for i in range(0,len(x),+1):
        result.append(x[i])
        result.append(y[i])
    print(result)
        
is_merge(x= [1, 2, 3],y= ['a', 'b', 'c'])