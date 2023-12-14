import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

t = 0
for k in range(len(grid[0])):
    jstart = 0
    num_stones = 0
    for j in range(len(grid)):
        if grid[j][k] == '#':
            for c in range(num_stones):
                t += (len(grid) - jstart - c)
            num_stones = 0
            jstart = j+1
        elif grid[j][k] == 'O':
            num_stones += 1
    for c in range(num_stones):
        t += (len(grid) - jstart - c)
print(t)