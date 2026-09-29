#!/usr/bin/env python3
"""Module that creates a BaseGeometry Class"""


class BaseGeometry:
    """Base for all shapes"""

    def area(self):
        raise Exception("area() is not implemented")
