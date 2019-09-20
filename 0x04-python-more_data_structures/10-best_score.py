#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best = 0
        for key, item in a_dictionary.items():
            if item > best:
                best = item
                name = key
    return name
