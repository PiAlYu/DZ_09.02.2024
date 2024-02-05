def f(a, b):
    if a == b: return 1
    if a > b or a == 32: return 0
    return f(a + 3, b) + f(a * 2, b)

print(f(1, 16) * f(16, 41))
