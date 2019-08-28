# Given an array of integers, return a new array such that 
# each element at index i of the new array is the product of 
# all the numbers in the original array except the one at i

def product_of_list(list_):
    result_list = []
    for i in range(len(list_)):
        throw_away = list_.copy()
        throw_away.pop(i)
        result = 1
        for i in throw_away:
            result = result * i
        result_list.append(result)
    return result_list


array = [1,2,3,4,5]
print(product_of_list(array))
