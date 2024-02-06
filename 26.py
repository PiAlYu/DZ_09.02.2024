fin = open('26.txt')
a = fin.readlines()
fin.close()
n, s = a.pop(0).split()
s = int(s)
a = [int(i) for i in a]
a.sort()
for i in range(len(a)):
    if s > a[i]:
        s -= a[i]
    else:
        print(i, s + a[i - 1])
        break
