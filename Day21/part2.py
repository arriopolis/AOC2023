import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

assert len(grid) == len(grid[0])

for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c == 'S':
            startx,starty = x,y

assert all(grid[starty][x] != '#' for x in range(len(grid)))
assert all(grid[y][startx] != '#' for y in range(len(grid)))

steps = {}
starts = it.product([0,startx,len(grid[0])-1], [0,starty,len(grid)-1])
for start in starts:
    frontier = set([start])
    visited = set()
    steps[start] = []
    while frontier:
        num_poss = len(frontier)
        if len(steps[start]) >= 2: num_poss += steps[start][-2]
        steps[start].append(num_poss)
        new_frontier = set()
        for x,y in frontier:
            visited.add((x,y))
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                newx,newy = x+dx,y+dy
                if not 0 <= newx < len(grid[0]): continue
                if not 0 <= newy < len(grid): continue
                if grid[newy][newx] == '#': continue
                if (newx,newy) in visited: continue
                new_frontier.add((newx,newy))
        frontier = new_frontier

num_steps = 26501365

tot = 0
for start,step_dct in steps.items():
    if start == (startx,starty):
        if num_steps < len(step_dct):
            tot += step_dct[num_steps]
        else:
            tot += step_dct[num_steps%2::2][-1]
    
    elif start[0] == startx or start[1] == starty:
        if start == (startx,0): init_steps = len(grid) - starty
        elif start == (startx,len(grid)-1): init_steps = starty + 1
        elif start == (0,starty): init_steps = len(grid) - startx
        elif start == (len(grid[0])-1,starty): init_steps = startx + 1

        if start[0] == startx: l = len(grid)
        elif start[1] == starty: l = len(grid[0])

        s = num_steps - init_steps
        if s < 0: continue
        n = s // l
        s -= l*n

        while n >= 0 and s < len(step_dct):
            tot += step_dct[s]
            s += l
            n -= 1
        
        if n >= 0:
            tot += (n//2+1)*step_dct[s%2::2][-1]
            tot += (n//2)*step_dct[1-s%2::2][-1]
    
    else:
        x,y = start
        x = len(grid[0])-1-x
        y = len(grid)-1-y
        init_steps = abs(startx-x) + abs(starty-y) + 2
        l = len(grid)
        
        s = num_steps - init_steps
        if s < 0: continue
        n = s // l
        s -= l*n
        
        while n >= 0 and s < len(step_dct):
            tot += (n+1)*step_dct[s]
            s += l
            n -= 1

        if n >= 0:
            even_steps = n//2
            odd_steps = (n-1)//2
            tot += (even_steps+2)*(even_steps+1) * step_dct[s%2::2][-1]
            tot += (odd_steps+1)**2 * step_dct[1-s%2::2][-1]
print(tot)