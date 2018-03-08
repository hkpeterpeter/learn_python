#!/usr/bin/env python3

# There is a special note of using default value
# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list,
# dictionary, or instances of most classes. For example, the following function
# accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1,2]
print(f(3))  # [1,2,3]

# avoid L share among function invokes
def g(a, L=None):
    if L is None:
        L = []    # every function call, L becomes []
    L.append(a)
    return L

print(g(1))  # [1]
print(g(2))  # [2]
print(g(3))  # [3]

