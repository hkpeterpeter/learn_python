#!/usr/bin/env python3

i = 0
print("Using while", end=": ")
while i<5:
    print(i,end=",")
    i = i + 1
print()

print("Using for with range", end=": ")
for i in range(0, 5):
    print(i, end=',')
print()

print("Using for with range (v2)", end=": ")
for i in range(1, 10, 2):
    print(i, end=",")
print()

print("Using for with list", end=": ")
items = [1, "hello", [1,2,3], 2.5]
for x in items:
    print(x, end=",")
print()

# dummy loop
for x in range(1,100):
    pass # using pass, do nth