#!/usr/bin/env python3

def best_score(a_dictionary):
    best_key = ""
    best = 0

    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
            best_key = key
    
    return best_key
