import math

def area(a, b, c):
    half_peri = (a + b + c) / 2
    return math.sqrt(half_peri * (half_peri - a) * (half_peri - b) * (half_peri - c))


def perimeter(a, b, c):
    return a + b + c
