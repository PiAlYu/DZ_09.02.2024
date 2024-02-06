fin = open('17 (1).txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
k, c, ma = 0, 0, -float('inf')
for i in range(len(a)):
    if abs(a[i]) < 100:
        k += 1
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) / 2 > k:
        ma = max(ma, a[i] + a[i + 1])
        c += 1
print(c, ma)
