#!/usr/bin/env python3

str = 'string1'  # single quote or
str2 = "string2"  # double quote

# string, spanning multiple lines
str3 = """Line 1
Line 2
Line 3
"""

print(str)
print(str2)
print(str3)
print(str + str2) # string concat
print(str * 2)  # repeat as "string1string1"
print(str[0]) # The first char
print(str[-1]) # The last char
print(str[:])   # The whole string
print(str[1:])  # [1..end)
print(str[-2:])  # [end-2..end), the last 2 characters
print(str[-3:-1]) # [end-3..end-1)
print(str[::2])  # str[0] str[2] str[4]...
print(str[1::2])  # str[1], str[3]...

# Index out of range
try:
    print(str[-1000]) # exception, IndexError
except IndexError as e:
    print("IndexError: ", e)

# Python string is immutable
try:
    str[0] = 'H'
except TypeError as e:
    print("TypeError: ", e)




