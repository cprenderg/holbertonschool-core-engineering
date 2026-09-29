#!/usr/bin/env python3
"""Module that contains the square class"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Insides of the square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
