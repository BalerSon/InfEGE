"""Перевод в любую систему счисления"""

def to_ternary(n):
    t = ''
    while n > 0:
        t = t + str(n % 3)
        n //= 3
    t = t[::-1]
    return t

m = 10**1000

for n in range(167, 1000):
    t = to_ternary(n)
    summ = sum(int(i) for i in t)
    if summ % 9 == 0:
        t = t + '2'
    else:
        t = t + to_ternary(summ % 9)
    r = int(t, 3)
    m = min(m, r)
print(m)