def greedy_ratio(list_):
    new = []
    for w, l in list_:
        new.append(w / l)
    new.sort()
    return new


def greedy_diff(list_):
    new = []
    for w, l in list_:
        new.append(w - l)
    new.sort()
    return new


test = [[3, 5], [1, 2]]

print(greedy_ratio(test))
print(greedy_diff(test))
