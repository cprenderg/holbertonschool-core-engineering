#!/usr/bin/env python3
"""Module that creates a square object"""


class Square:
    """Insides of a square class"""

    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
