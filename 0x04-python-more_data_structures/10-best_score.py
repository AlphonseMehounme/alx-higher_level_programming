#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    lit = list(a_dictionary)
    best = lit[0]
    score = a_dictionary[best]
    for i in lit:
        if a_dictionary[i] > score:
            best = i
    return best
