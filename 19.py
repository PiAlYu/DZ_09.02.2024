from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 2, b), (a, b * 2), (a * 2, b), (a, b + 2)

@lru_cache(None)
def game(h, x):
    if sum(h) >= x:
        return "end"
    if any(game(y, x) == "end" for y in moves(h)):
        return "p1"
    if all(game(y, x) == "p1" for y in moves(h)):
        return "v1"

for i in range(1, 340):
    h = (4, 9)
    if game(h, i) == "v1":
        print(i, game(h, i))
        break
