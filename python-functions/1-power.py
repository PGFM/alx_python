#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
<<<<<<< HEAD
    return {a**b}
    # return round(result, 10)  # round to 10 decimal places
=======

