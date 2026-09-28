#!/usr/bin/env python3
"""Module that creates a square object"""


class Square:
    def __init__(self, size):
        """Insides of a square class"""
        try:
            self.__size = size
        except TypeError:
            TypeError("size must be an integer")
        except ValueError:
            ValueError("size must be >= 0")
