from itertools import product

def f(n):
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i], 15) % 2 != 0:
                return False
        elif int(n[i], 15) % 3 != 0:
            return False
    return True

def f1(n):
    for i in range(len(n)):
        if i % 2 == 1:
            if int(n[i], 15) % 2 != 0:
                return False
        elif int(n[i], 15) % 3 != 0:
            return False
    return True

k = 0
for i in product('0123456789abcde', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and (f(s) == True or f1(s) == True):
        k += 1
print(k)
