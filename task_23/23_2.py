q = []
def f(a,k):
    if k == 11:
        q.append(a)
        return 1
    return f(a+1,k+1) + f((a*2)+1,k+1)
f(3,0)
print(len(q))
