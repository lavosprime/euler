import math

def gcf(a, b):
    """Return the greatest common factor of two integers."""
    a, b = max(a, b), min(a, b)
    while b is not 0:
        a, b = b, a % b
    return a

gcd = gcf

def lcm(a, b):
    """Return the least common multiple of two integers."""
    return a * b / gcf(a, b)