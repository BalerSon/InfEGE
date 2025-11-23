from functools import *

@lru_cache(None)

def f(a, b, k1, k2, k3):
    if k1 > 4 or k3 > 5: return 0
    if a == b:
        if k1 <= 4 and k2 >= 2 and k3 == 5: return 1
        else: return 0
    if a > b: return 0
    if a < b: return f(a * 5, b, k1 + 1, k2, k3) + f(a * 3, b, k1, k2 + 1, k3) + f(a + 45, b, k1, k2, k3 + 1)
print(f(1, 2970, 0, 0, 0))
