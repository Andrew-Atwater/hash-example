import math

def hash(k, m = 1000):
    A = (math.sqrt(5) - 1) / 2
    frac = (k * A) % 1
    return int (m * frac)

val_arr = [71, 72, 73, 74, 75]
hashing = {k: hash(k) for k in val_arr}

for k in hashing:
    print(f"h({k}) = {hash(k)}")

