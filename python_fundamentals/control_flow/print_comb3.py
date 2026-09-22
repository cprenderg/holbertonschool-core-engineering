#!/usr/bin/env python3

printed = []
skip = 0

for x in range(99):
    skip = 0
    for num in printed:
        if x % 10 != int(x / 10):
            if x % 10 == num % 10 or x % 10 == int(num / 10):
                if int(x / 10) == int(num / 10) or int(x / 10) == num % 10:
                    skip = 1
        if x > 10 and x % 10 == 0:
            skip = 1
    if skip == 0:
        if x == 89:
            print("{:02d}".format(x))
        else:
            print("{:02d}, ".format(x), end="")
        printed.append(x)
