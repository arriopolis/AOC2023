import sys
import itertools as it

N = int(1e6)-1

grid = []
for line in sys.stdin:
    grid.append(list(map(lambda x : x == '#', line.strip())))

rows = []
num_rows = 0
for j,r in enumerate(grid):
    if not any(r):
        num_rows += 1
    rows.append(num_rows)

cols = []
num_cols = 0
grid = list(map(list, zip(*grid)))
for j,r in enumerate(grid):
    if not any(r):
        num_cols += 1
    cols.append(num_cols)
grid = list(map(list, zip(*grid)))

orig_points = set()
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c: orig_points.add((x,y))

points = set()
for x,y in orig_points:
    newx = x + cols[x]*N
    newy = y + rows[y]*N
    points.add((newx,newy))

s = 0
for (x1,y1),(x2,y2) in it.product(points, repeat = 2):
    d = abs(x1-x2) + abs(y1-y2)
    s += d
print(s//2)