#!/usr/bin/env python3

# Recommendation: using with
# Benefit: auto-close after the with clause

fname = "input.txt"
with open(fname) as f:
    print("== Content of {} ==".format(fname))
    for line in f:
        print(line, end="")
    print()
print("{} is closed ? {}".format(fname, f.closed))

import json
outName = "out1.txt"
with open(outName, "w") as f:
    arr = [1, {"Hello": 5, 4: "Value"}, [4,5, (5,6)]]
    json.dump(arr, f)

print("{} is closed ? {}".format(outName, f.closed))

with open(outName) as f:
    print( json.load(f) )

print("{} is closed ? {}".format(outName, f.closed))



