#!/usr/bin/env python3

# Search path:
#  1. Build-in module
#  2. Search sys.path = current dir + PYTHONPATH

import sys

print("sys.path = ", sys.path)

# Relative to the project root
import python_tutorials.fib

# Not easy to use it
print(python_tutorials.fib.fib(5))
python_tutorials.fib.print_fib(5)

# A better way to import
from python_tutorials.fib import fib, print_fib

print(fib(5))
print_fib(5)

# Avoiding name conflicts using as
from python_tutorials.fib import fib as fibRenamed, print_fib as pfib

print(fibRenamed(5))
pfib(5)
