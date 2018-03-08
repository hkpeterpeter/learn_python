#!/usr/bin/env python3

# Special notes when using Python loop

wordList = ["Hello", "World", "Peter"]

# normal usage
print("wordList = ", end="")
for w in wordList:
    print(w, end=", ")
print("\n", wordList,"\n")

# iteration with list mutation
print("wordList = ", end="")
# create a new copy of list for iteration
# Otherwise, infinite loop
for w in wordList[:]:
    print(w, end=", ")
    wordList.append(w)
print("\n", wordList, "\n")