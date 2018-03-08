#!/usr/bin/env python3

empty = {}
empty = dict()   # both syntax are empty dictionary
d = {1: "Hello", 5: "John", 7: "value", "err": 5}

print("empty = ", empty)
print("d = ", d)

# keys, values, items
print("keys: ", list(d.keys()))
print("values: ", list(d.values()))
print("items: ", list(d.items()))

# comprehension
compd = { str(x): x*x for x in range(1,6) }
print("compd =", compd)

# using with for
for k in d.keys():
    print(k, end=" ")
print()

for v in d.values():
    print(v, end=" ")
print()

for k, v in d.items():
    print( "{key}:{value}".format(key=k,value=v), end=" " )
print()

for i, v in enumerate(d):
    print( "{index}:{value}".format(index=i,value=v), end=" ")
print()

# Using zip
nums = [1,2,3,4]
strs = ["Hello", "world", "abc", "def"]
for n,s in zip(nums, strs):
    print("{}:{}".format(n,s), end=" ")
print()



