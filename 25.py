from fnmatch import fnmatch

for i in range(130000, 10 ** 9, 13):
    if fnmatch(str(i), '24*68?35'):
        if int(str(i)[-3]) % 3 == 0 and int(str(i)[-3]) % 2 == 1:
            s = str(i)[2:-3]
            if all(int(j) % 2 == 0 for j in s) or len(s) == 0:
                print(i, i // 13)
