fin = open('24.txt')
s = fin.readline()
fin.close()
k = 0
for i in range(2, len(s) - 2):
    a = s[i - 2: i + 3]
    b = s[i: i + 3]
    if b == 'OCK' and a != 'STOCK':
        k += 1
print(k)
