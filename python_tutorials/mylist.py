#!/usr/bin/env python3

# Defining lists
intList = [1, 2, 3, 4, 5]
strList = ["hello", "world"]
anyList = [1, "hello", 4.5]
nestedList = [ intList, strList, anyList, 1, 2]

print(intList)
print(strList)
print(anyList)
print(nestedList)

# Unlike string, list is mutable

list = intList          # assign
list.append(99)      # append
list.insert(0, 123)  # insert
print(list)
print(len(list))       # length of the list
print(list + strList) # list concat
