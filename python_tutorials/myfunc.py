#!/usr/bin/env python3

# A dummy function, do nth
def dummy():
    """
    This is the documentation of dummy
    :return: nothing
    """
    pass


dummy()  # invoke a dummy function
print(dummy.__doc__)


print("function with keyword arguments")
def f(a=1, b=2, c=3):
    print("(a,b,c) = ", a, ",", b, ",", c)

f(1, 2, 3)
f(c=3, a=1, b=2)

print("unpacking arguments")
print( list(range(3,6)))
args = [3,6]
print( list(range(*args)))


# A sample usage of position arguments and keyword arguments
def ask_ok(prompt, retries=4, reminder='Please try again'):
    """
    Prompt user to say Yes/No
    :param prompt: The prompt message
    :param retries: The number of retry. Default=4
    :param reminder: The reminder message
    :return:
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Too many retries')
        print(reminder, retries, 'remaining retries')


print(ask_ok('Enter (y/n): ', retries=10))
