#!/usr/bin/env python3

def pow(a, b):
    c = a
    if b == 0:
        return 1
    for x in range(1, abs(b)):
        c *= a
    if b < 0:
        return 1 / c
    return c
