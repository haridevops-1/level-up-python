def find_higher_average(gen_list, marks_list):
    male_sum = 0
    female_sum = 0
    male_count = 0
    female_count = 0

    for i in range(len(gen_list)):
        if gen_list[i] == 'M':
            male_sum += marks_list[i]
            male_count += 1
        else:
            female_sum += marks_list[i]
            female_count += 1

    male_avg = male_sum / male_count
    female_avg = female_sum / female_count

    if male_avg > female_avg:
        print("Male", male_avg)
    else:
        print("Female", female_avg)


def numbers_between_two_zeros(arr):
    start = -1
    result = []
    collect = False   

    for i in range(len(arr)):
        if arr[i] == 0:
            if start == -1:
                start = i
                collect = True      
            else:
                collect = False   
                break              
        elif collect and start != -1:
            result.append(arr[i])


    if collect:
        return -1

    print(result)


def bracket_match(bracket_string):
    count = 0
    for ch in bracket_string:
        if count < 0:
            print(False)
            return
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1

    if count == 0:
        print(True)
    else:
        print(False)