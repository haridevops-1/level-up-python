# You are given two lists:

# One list shows the gender of each student ('M' for male, 'F' for female).

# The other list shows their marks in the same order.

# Write a Python program to:

# Find the average marks of male students.

# Find the average marks of female students.

# Print "Male <average>" if male students have the higher average, or "Female <average>" if female students have the higher average.




def find_higher_average(gen_list, marks_list):
    male_sum = 0
    female_sum = 0
    male_count = 0
    female_count = 0
    #start
    for i in range(0, len(gen_list),+1):
        if gen_list[i] == 'M':
            male_sum= male_sum + marks_list[i]
            male_count +=1
            # print(male_sum)
        else:
            female_sum = female_sum + marks_list[i]
            female_count += 1
            # print(female_sum)

    male_avg = male_sum / male_count
    female_avg = female_sum / female_count

    #stop

    if male_avg > female_avg:
        print("male_average", male_avg)
    else:
        if female_avg > female_count:
            print("female_count", female_avg)

    
find_higher_average(['M','F','M','F','M','F','M'],
                    [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])










find_higher_average(['M','F','M','F','M','F','M'],
                    [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0])

find_higher_average(['M','F','M','F','M','F','M'],
                    [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])