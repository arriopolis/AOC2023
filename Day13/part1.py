import sys

grids = []
grid = []
for line in sys.stdin:
    if not line.strip():
        grids.append(grid)
        grid = []
    else:
        grid.append(list(line.strip()))
grids.append(grid)

t = 0
for grid in grids:
    for j in range(1,len(grid)):
        l = min(j, len(grid)-j)
        if grid[j-l:j] == grid[j+l-1:j-1:-1]:
            t += j*100
    grid = list(zip(*grid))

    for j in range(1,len(grid)):
        l = min(j, len(grid)-j)
        if grid[j-l:j] == grid[j+l-1:j-1:-1]:
            t += j
    grid = list(zip(*grid))
print(t)