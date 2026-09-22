#!/usr/bin/env python3

def uppercase(str):
    letter = 0
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            letter = ord(c) - 32
        else:
            letter = ord(c)
        print("{:c}".format(letter), end="")
    print("")

uppercase("TeSt")