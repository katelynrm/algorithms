
V = ['a','b','c','d']
E = {('a','b'):1, ('b','c'):2, ('c','d'):3, ('a','c'):4, ( 'b','d'):6}

G = (V,E)

X = dict()
a = 0
X['a'] = a

for e,l in E.items():
    v, w = e[0], e[1]
    while v in X and w not in X:
        #v, w = e[0], e[1]
        X[w] = l
        print(e,l)

print(X)