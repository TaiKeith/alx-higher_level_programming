#!/usr/bin/python3
x = 0
for i in range(122, 96, -1):
    x = i
    if (i % 2 != 0):
        x = i - 32
    print("{}".format(chr(x)), end='')
