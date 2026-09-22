#!/usr/bin/env python3

def uppercase(str):
    upperstr = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            upperstr += (chr(ord(c) - 32))
        else:
            upperstr += c
    print(upperstr)

