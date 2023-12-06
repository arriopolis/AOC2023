import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(line.strip())

poss = {}
specials = []
for j,r in enumerate(grid):
    for k,c in enumerate(r):
        if (j,k) in poss: continue
        if c in '0123456789':
            num = 0
            for d,c in enumerate(r[k:]):
                if c not in '0123456789': break
                num = 10*num + int(c)
            coords = set([(j,k2) for k2 in range(k,k+d)])
            for j2,k2 in coords:
                poss[(j2,k2)] = (num, coords)
        elif c == '*':
            specials.append((j,k))

s = 0
for j,k in specials:
    added = set()
    ctr = 0
    prod = 1
    for dj,dk in it.product(range(-1,2), repeat = 2):
        newj,newk = j+dj,k+dk
        if (newj,newk) in added: continue
        if (newj,newk) in poss:
            ctr += 1
            num, to_add = poss[(newj,newk)]
            added.update(to_add)
            prod *= num
    if ctr == 2:
        s += prod
print(s)