# Given an array of integers and a number k, 
# where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

#     10 = max(10, 5, 2)
#     7 = max(5, 2, 7)
#     8 = max(2, 7, 8)
#     8 = max(7, 8, 7)

def subarray_max(array, k):
    for i in range(0,(len(array) - (k-1))):
        subarray = array[i:i+k]
        print(max(subarray))


array_ = [10, 5, 2, 7, 8, 7]

print(subarray_max(array_,3))