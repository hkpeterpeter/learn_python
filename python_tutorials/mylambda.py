#!/usr/bin/env python3

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
for v in [0,1,2]:
    print( f(v), end="," )
print()


pairs = [(1, 'one'),  (3, 'three'), (2, 'two'), (4, 'four')]

# Sort by the first value
pairs.sort(key=lambda pair: pair[0])
print(pairs)

# Sort by the second value
pairs.sort(key=lambda pair: pair[1])
print(pairs)