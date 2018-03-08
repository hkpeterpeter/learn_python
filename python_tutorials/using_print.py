#!/usr/bin/env python3

# Using end as a keyword argument
print("result", end=": ")

# Values in different types can be separated by commas
print("commas ", 1, " " , 2.5, " ", [1,2,3], end="\n" )

# print - using sep
print(1,2,3,4,5,sep="| ", end="\n")

# print - using format
print("{},{}".format(1,2))
print("{1},{0}".format(1,2))   # positional
print("(x,y) = ({x},{y})".format(y=2, x=1))

# print - using zfill
print(str(20).zfill(5))

# print - using % (old style)
print("%05d %s %.3f" % (20, "Hello",2.4) )

# using resp and rjust
for x in range(1, 4):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
print()

# equivalent using format
for x in range(1, 4):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print()