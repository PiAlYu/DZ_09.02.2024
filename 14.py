for x in 'cba9876543210':
    a = int(f'537{x}623', 13)
    b = int(f'6{x}35{x}2', 13)
    if (a - b) % 3 == 0:
        print(int(x, 13))
        break
