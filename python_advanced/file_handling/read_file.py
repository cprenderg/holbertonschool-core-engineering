#!/usr/bin/env python3

""" This function reads a file and returns if the file has been closed """


def read_file(filename=""):

    """ This function reads a file and returns if the file has been closed """

    with open(filename) as f:
        for line in f:
            print(line, end='')
    return f.closed
