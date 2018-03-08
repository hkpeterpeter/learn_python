#!/usr/bin/env python3

# Recommendation: using list as stack
print("stack demo:")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

# Recommendation: using collections.deque
from collections import deque
print("queue demo:")
queue = deque([3,4,5])
queue.append(6)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)