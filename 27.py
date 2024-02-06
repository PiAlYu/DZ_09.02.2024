# работатет за 0.22340083122253418
from copy import copy

fin = open('27B.txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
n = a.pop(0)
ma, k = -float('inf'), 1
b = copy(a)
b.sort(key = lambda x: -x)
for i in range(n):
    if i < 5:
        o = a[:i + 6]
    else:
        o = a[i - 5:i + 6]
    o1 = copy(o)
    for j in range(12):
        if b[j] in o:
            o.remove(b[j])
        else:
            if b[j] + a[i] == ma:
                k += b.count(b[j]) - o1.count(b[j])
            elif b[j] + a[i] > ma:
                ma = b[j] + a[i]
                k = b.count(b[j]) - o1.count(b[j])
            break
print(k // 2)
