def check_numbers(master_list: list[int], current_list: list[int]):
    if len(master_list) == 0:
        print("Invalid Input")
    else:
        result = 0
        for el in master_list:
            if el not in current_list:
                result = el
        return result
check_numbers([10,20,30,40,50],[10,20,40,50])