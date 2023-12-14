import sys

T = 1000000000

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

visited = {}
hist = []
i = 0
while tuple(map(tuple,grid)) not in visited:
    visited[tuple(map(tuple,grid))] = i
    for _ in range(4):
        new_grid = [['.']*len(grid[0]) for _ in grid]
        for k in range(len(grid[0])):
            jctr = 0
            for j in range(len(grid)):
                if grid[j][k] == '#':
                    new_grid[j][k] = '#'
                    jctr = j+1
                elif grid[j][k] == 'O':
                    new_grid[jctr][k] = 'O'
                    jctr += 1
        grid = list(zip(*reversed(new_grid)))
    
    t = 0
    for j,r in enumerate(grid):
        for k,c in enumerate(r):
            if c == 'O': t += len(grid) - j
    hist.append(t)
    
    i += 1

start_loop = visited[tuple(map(tuple,grid))]
period = i - start_loop
print(hist[(T-start_loop-1)%period + start_loop])