print('x y z w f')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not(x)) <= y) and ((not(y)) == z) and w
                if f == True:
                    print(x, y, z, w, f)
