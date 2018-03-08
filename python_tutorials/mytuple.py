#!/usr/bin/env python3

# Tuple is non-mutable in Python

t = 1, "Hello", 2.4
empty = ()       # alternative: empty = tuple()
singleton = 1,   # a special syntax for a single tuple

print("t = ", t)
print("empty = ", empty)
print("singleton = ", singleton)
print("len(t) = ", len(t))

# unpacking tuple
x, y, z = t
print("x = ", x)
print("y = ", y)
print("z = ", z)

# Although tuple is immutable, it can store mutable objects
tupleOfList = ( [1,2,3], [4,5,6] )
print("tupleOfList = ", tupleOfList)
vec1, vec2 = tupleOfList                 # unpacking
vec1[0] = 9                              # modify vec1
vec2.append(2)                           # append vec2
print("tupleOfList = ", tupleOfList)
