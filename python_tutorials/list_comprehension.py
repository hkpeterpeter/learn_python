#!/usr/bin/env python3

# Techniques to build a list

print("Not recommend to use append:")

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

print("Recommend to use map + lambda:")
squares = list(map(lambda x: x**2, range(10)))
print(squares)

print("Equivalent using for ... in syntax:")
squares = [x**2 for x in range(10)]
print(squares)

print("Build a 2D array using nested for..in")
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

print("Equivalent using nested for... in loop")
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)


print("create a list of 2-tuples like (number, square)")
listTuples = [(x, x**2) for x in range(6)]
print(listTuples)


print("flatten a list using a listcomp with two 'for'")
vec = [[1,2,3], [4,5,6], [7,8,9]]
print(vec)
flatVec = [num for elem in vec for num in elem]
print(flatVec)

from math import pi
piList = [str(round(pi, i)) for i in range(1, 6)]
print(piList)
