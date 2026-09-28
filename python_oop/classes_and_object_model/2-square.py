#!/usr/bin/env python3
"""Module that creates a square object"""


class Square:
    """Insides of a square class"""

    def __init__(self, size):
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
