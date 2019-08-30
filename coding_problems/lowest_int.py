# Given an array of integers, find the first missing positive 
# integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

def find_lowest_int(list_):
    new_list = []
    for i in list_:
        if i > 0:
            new_list.append(i)
    for i in range(1, max(new_list)):
        if i not in new_list:
            return i
        elif len(new_list) == max(list_):
            return len(new_list) + 1

my_list = [-9,8,1,2,3,4]
print(find_lowest_int(my_list))