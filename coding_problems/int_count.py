# Given an array of integers where every integer occurs three times
# except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.


def int_count(list_):
    result = dict()
    for i in list_:
        if i not in result:
            result[i] = 1
        else:
            result[i] = result[i] + 1
    for k, v in result.items():
        if v == 1:
            return k


my_list = [6, 1, 3, 3, 3, 6, 6]
print(int_count(my_list))
