#!/usr/bin/env python3

# break, continue and else

print("Find prime form 2..9:")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, '*', n//x)
            break
    else:
        # Note: this else clause belongs to the loop
        print(n, 'is a prime number')


print("List out odd/even from 2..9:")
for n in range(2, 10):
    if n % 2 == 0:
        print(n, "is even")
        continue # using continue here
    print(n, "is odd")