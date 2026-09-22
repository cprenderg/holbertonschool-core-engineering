#!/usr/bin/env python3

for x in range (90):
    if int(x / 10) < x % 10:
        if x == 89:
            print("{:02d}".format(x))
        else:
            print("{:02d}, ".format(x), end="")
