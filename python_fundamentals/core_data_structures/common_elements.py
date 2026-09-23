#!/usr/bin/env python3

def common_elements(set_1, set_2):
    matches = []

    for item1 in set_1:
        for item2 in set_2:
            if item1 == item2:
                matches.append(item1)
    return matches
