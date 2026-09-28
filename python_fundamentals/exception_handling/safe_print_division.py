#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        ans = a / b
    except ZeroDivisionError:
        ans = None
    finally:
        print(f"Inside result: {ans}")
    return ans
