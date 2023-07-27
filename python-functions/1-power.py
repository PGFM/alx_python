#!/usr/bin/python3
# def pow(a, b):
#     result = 1
#     if b < 0:
#         a = 1 / a
#         b = abs(b)
#     for _ in range(b):
#         result *= a
#     return result
def pow(a, b, precision=10):
    result = 1
    if b < 0:
        a = 1 / a
        b = abs(b)
    for _ in range(b):
        result *= a
    return round(result, precision)