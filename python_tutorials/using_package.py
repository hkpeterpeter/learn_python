#!/usr/bin/env python3

#
# from [package].[subpackage].[module] import [stuff]
#
from python_tutorials.demopack.subpack.hello \
    import hello as h, world as w

print(h())
print(w())