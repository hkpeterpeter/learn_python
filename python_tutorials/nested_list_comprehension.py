#!/usr/bin/env python3

# Techniques of building nested list

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("Flattening a 2D matrix")
result = [val for row in matrix for val in row]
print(result)

print("transpose rows and columns")
result = [[row[i] for row in matrix] for i in range(4)]
print(result)

print("Unpacking argument using *")
print(*matrix)
print(matrix[0], matrix[1], matrix[2])

print("zip to construct list of tuples")
# here, * will unpack the argument list
result = list(zip(*matrix))
print(result)
