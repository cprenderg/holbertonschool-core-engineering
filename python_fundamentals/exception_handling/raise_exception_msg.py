#!/usr/bin/env python3

def raise_exception_msg(message=""):
    try:
        print("{}".format(x))
    except NameError:
        raise NameError(message)
