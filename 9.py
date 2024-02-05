class Digit:
    def __init__(self, x1, x2, x3, x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
    def a(self):
        l = [self.x1, self.x2, self.x3, self.x4]
        return (max(l) + min(l)) % 3 == 0
    def b(self):
        l = [self.x1, self.x2, self.x3, self.x4]
        for a in range(len(l)):
            for b in range(len(l)):
                for c in range(len(l)):
                    for d in range(len(l)):
                        if len(set([a, b, c, d])) == 4:
                            if abs(l[a] - l[b]) == abs(l[c] - l[d]):
                                return True
        return False

fin = open('09.csv')
s = fin.readlines()
fin.close()
s = [list(map(int, i.split(';'))) for i in s]
print(s)
a, k = [], 0
for i in s:
    a.append(Digit(i[0], i[1], i[2], i[3]))
for i in a:
    if i.a() and i.b() == True:
        k += 1
print(k)
