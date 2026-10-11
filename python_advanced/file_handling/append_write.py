#!/usr/bin/env python3

""" This function writes appends to a file and returns the
number of characters written """


def append_write(filename="", text=""):

    """ This function writes appends to a file and returns the
    number of characters written """

    with open(filename, "a+") as f:
        return f.write(text)
