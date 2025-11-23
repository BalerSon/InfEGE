from itertools import *

"""Решение с выводом окончательного ответа"""

def f(x, y, z, w):
    return not(x <= z) or (w <= (y == z))

for a in product([0, 1], repeat = 7):
    table = [(a[0], a[1], 0, 0), (a[2], 1, a[3], a[4]), (a[5], 0, a[6], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
