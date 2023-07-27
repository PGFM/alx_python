#!/usr/bin/python3
# def pow(a, b, precision=15):
#     result = 1
#     if b < 0:
#         a = 1 / a
#         b = abs(b)
#     for _ in range(b):
#         result *= a
#     return round(result, precision)
from decimal import Decimal, getcontext

def pow(a, b):
    getcontext().prec = 28  # Set precision to a sufficient value
    result = Decimal(1)
    if b < 0:
        a = 1 / a
        b = abs(b)
    for _ in range(b):
        result *= Decimal(a)
    return float(result)
