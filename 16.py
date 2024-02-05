from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 10000: return 1
    if n % 2 == 0: return f(n + 3) + 7
    return f(n + 1) - 3

a = []
for i in range(9999, 49, -1):
    a.append(f(i))
print(a[-1] - a[-8])
