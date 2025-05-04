import math

def hash(k, m = 1000):
    A = (math.sqrt(5) - 1) / 2
    frac = (k * A) % 1
    return (m * frac)

