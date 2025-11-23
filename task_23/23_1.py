from functools import *
@lru_cache(None)
def f(a,b,k):
    if a > b: return 0
    if a == b: return 1 if k % 2 != 0 else 0
    if a < b and a != 1:
        return f(a + 2, b, k + 1) + f(a * 2, b, k + 1) + f(a ** 2, b, k + 1)
    else:
        return f(a + 2, b, k + 1) + f(a * 2, b, k + 1)
print(f(1,100,0))
