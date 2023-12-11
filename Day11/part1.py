import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(list(map(lambda x : x == '#', line.strip())))

for _ in range(2):
    to_add = set()
    for j,r in enumerate(grid):
        if not any(r):
            to_add.add(j)
    for j in sorted(to_add, reverse = True):
        grid.insert(j, [False]*len(grid[0]))
    
    grid = list(map(list, zip(*grid)))

points = set()
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c: points.add((x,y))

s = 0
for (x1,y1),(x2,y2) in it.product(points, repeat = 2):
    d = abs(x1-x2) + abs(y1-y2)
    s += d
print(s//2)