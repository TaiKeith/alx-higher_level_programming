#!/usr/bin/python3

def magic_calulation(a, b):
    result = 0
    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception("Too far")
            else:
                result += (a ** b) / x
        except Exception:
            result = a + b
            break
    return result
