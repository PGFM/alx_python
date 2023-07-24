#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        combination = "{:02d}".format(a * 10 + b)
        if a == 8 and b == 9:
            print(combination, end="")
        else:
            print(combination, end=", ")
print("\n")