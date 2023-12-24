import sys

dirs = {
    '>' : (1,0),
    '<' : (-1,0),
    '^' : (0,-1),
    'v' : (0,1)
}

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

def DFS(pos, step_ctr = 0, visited = None):
    if visited is None: visited = set()
    x,y = pos
    if (x,y) == (len(grid[0])-2, len(grid)-1): return step_ctr
    
    while True:
        steps = set()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            newx,newy = x+dx,y+dy
            if not 0 <= newx < len(grid[0]): continue
            if not 0 <= newy < len(grid): continue
            if (newx,newy) in visited: continue
            if grid[newy][newx] == '#': continue
            dstep = 1

            if grid[newy][newx] in dirs:
                dx,dy = dirs[grid[newy][newx]]
                newx += dx
                newy += dy
                if not 0 <= newx < len(grid[0]): continue
                if not 0 <= newy < len(grid): continue
                if (newx,newy) in visited: continue
                if grid[newy][newx] == '#': continue
                dstep = 2
            steps.add((newx,newy,dstep))
        if len(steps) != 1: break
        x,y,dstep = steps.pop()
        step_ctr += dstep
        visited.add((x,y))
        if (x,y) == (len(grid[0])-2, len(grid)-1): return step_ctr
    
    m = 0
    for newx,newy,dstep in steps:
        new_visited = visited.copy()
        new_visited.add((newx,newy))
        m = max(m, DFS((newx,newy), step_ctr + dstep, new_visited))
    return m

print(DFS((1,0)))