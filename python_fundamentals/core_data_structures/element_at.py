#!/usr/bin/env python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    x = 0
    for item in my_list:
        x += 1
    if idx >= x:
        return None
    return my_list[idx]
