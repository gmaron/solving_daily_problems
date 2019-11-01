# Problem Day 4 (MEDIUM)

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# 
# Implement car and cdr.

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def cdr(fun):
    def f(a,b):
        return a
    return fun(f)

def car(fun):
    def f(a,b):
        return b    
    return fun(f)

print(cdr(cons(3,4)))
print(car(cons(3,4)))
