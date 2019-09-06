#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
my_list = [10, 15, 3, 7]
my_num = 40


#brute force
def product_in_list(list_, k):
    products_set = set()
    for i in list_:
        for j in list_[::-1]:
            if i != j:
                products_set.add(i+j)
    if k in products_set:
        return True
    else:
        return False


#hash table
def product_in_list_hash(list_,k):
    H = dict()
    for i in range(len(list_)):
        H[i] = list_[i]
    num = 0
    for i in range(len(list_)):
        y = k - list_[i]
        if y in H.values():
            num += 1
    if num > 0:
        return True
    else:
        return False

print(product_in_list(my_list, my_num))
print(product_in_list_hash(my_list, my_num))