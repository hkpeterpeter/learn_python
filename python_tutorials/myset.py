#!/usr/bin/env python3

emptySet = set()  # Can't use {}, reserved by an empty dictionary
s = {1, 2, 3, "Hello"}

print("s = ", s)
print("1 in s? ", 1 in s)
print("5 not in s? ", 5 not in s)

# set is mutable
s.add(6)
print("s = ", s)

# union and intersection
print(s.union({1, 2, 3, 4}))
print(s.intersection({1, 2, 3, 4}))

# set comprehension
myset = {x for x in "abckadeiiij" if x not in "acd"}
print("myset = ", myset)
valset = {(x,y) for x in range(1,3) for y in "ab"  }
print("valset = ", valset)