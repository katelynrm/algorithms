#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def add_any_two(list_, k):
    products_set = set()
    for i in list_:
        for j in list_[::-1]:
            if i != j:
                products_set.add(i+j)
    if k in products_set:
        return True
    else:
        return False

my_list = [10, 15, 3, 7]
my_num = 17

print(add_any_two(my_list, my_num))