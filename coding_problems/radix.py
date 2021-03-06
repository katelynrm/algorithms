
def radix_sort(array, base):
    main_bin = []
    depth = find_max_depth(array)
    base_bins = []

    for i in range(base):
        base_bins.append([])
    exp = 1
    for i in range(depth):
        main_bin.append([])
        for j in array:
            temp_index = j//exp%10
            base_bins[temp_index].append(j)
        exp = exp * base
        for l in base_bins:
            while l != []:
                main_bin[i].append(l.pop(0))

    return main_bin

def find_max_depth(array):
    return len(str(max(array)))

listofnums = [34, 967, 19, 888]
print(radix_sort(listofnums, 10))
