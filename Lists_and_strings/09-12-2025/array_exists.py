def array_exists(arr:list[int], k: int):
    if len(arr) == 0:
        print("Invalid Input")
    else:
        count = 0
        for el in range(0,len(arr),+1):
            if k == arr[el]:
                count =count +1 
        return count

array_exists([4,1,2,4,4,5,6,3,4])
