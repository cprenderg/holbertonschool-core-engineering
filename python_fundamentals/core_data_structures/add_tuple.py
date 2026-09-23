#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    arr = []
    i = 0
    if len(tuple_a) >= len(tuple_b) and i < len(tuple_a):
        while i < len(tuple_a):
            if not tuple_a[i]:
                x = 0
            else:
                x = tuple_a[i]
            if i < len(tuple_b):
                y = tuple_b[i]
            else:
                y = 0
            arr.append(x + y)
            i += 1
    elif len(tuple_b) > len(tuple_a) and i < len(tuple_b):
        while i < len(tuple_b):
            if not tuple_b[i]:
                y = 0
            else:
                y = tuple_b[i]
            if i < len(tuple_a):
                x = tuple_a[i]
            else:
                x = 0
            arr.append(x + y)
            i += 1
    if arr:
        if len(arr) == 1:
            arr.append(0)
        return (arr[0], arr[1])
    return (0, 0)
