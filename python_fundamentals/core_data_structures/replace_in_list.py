#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    x = 0
    for item in my_list:
        x += 1
    if idx >= x:
        return my_list
    my_list[idx] = element
    return my_list
