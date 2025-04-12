# PENTAGONAL NUMBERS

# x2 - x1 = xmin
# x2 + x1 = xmax

# Pn = n(3n - 1)/2


import numpy as np
import math

def is_integer_value(n):
    return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

def pentagonal_numbers_up_to(n):
    pentagonals = []
    for i in range(0,n):
        pentagonals.append(i*(3*i - 1)/2)
    return pentagonals

n = 10000
pentagonals = set(pentagonal_numbers_up_to(1000000))

for i in range(1,n):
    Pi = i * (3*i - 1) // 2
    for j in range(i+1,n):
        Pj = j * (3*j - 1) // 2
        if (Pj - Pi) in pentagonals and (Pj + Pi) in pentagonals:
            print(Pj - Pi, Pj, Pi, Pj + Pi)