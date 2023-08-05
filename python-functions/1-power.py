#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    if result.is_integer():
        return int(result)
    else:
        return float(format(result, '.22g'))  # format to 22 significant figures
