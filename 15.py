def f(n):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x > 39) or (y > 26) or (2 * x + 4 * y < n)
            if f == False:
                return False
    return True

for a in range(1000):
    if f(a) == True:
        print(a)
        break
