# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

#given cons
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def first(a,b):
        return a
    return f(first)


def cdf(f):
    def last(a,b):
        return b 
    return f(last)


print(car(cons(3, 4)))
print(cdf(cons(3, 4)))