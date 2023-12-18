import sys

dirs = {
    '.' : {
        (0,1) : set([(0,1)]),
        (1,0) : set([(1,0)]),
        (0,-1) : set([(0,-1)]),
        (-1,0) : set([(-1,0)])
    },
    '/' : {
        (1,0) : set([(0,-1)]),
        (0,-1) : set([(1,0)]),
        (0,1) : set([(-1,0)]),
        (-1,0) : set([(0,1)])
    },
    '\\' : {
        (1,0) : set([(0,1)]),
        (0,-1) : set([(-1,0)]),
        (0,1) : set([(1,0)]),
        (-1,0) : set([(0,-1)])
    },
    '|' : {
        (1,0) : set([(0,1),(0,-1)]),
        (-1,0) : set([(0,1),(0,-1)]),
        (0,1) : set([(0,1)]),
        (0,-1) : set([(0,-1)])
    },
    '-' : {
        (0,1) : set([(-1,0),(1,0)]),
        (0,-1) : set([(-1,0),(1,0)]),
        (1,0) : set([(1,0)]),
        (-1,0) : set([(-1,0)])
    }
}

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

starts = []
for starty in range(len(grid)):
    starts.append(((-1,starty),(1,0)))
    starts.append(((len(grid[0]),starty),(-1,0)))
for startx in range(len(grid[0])):
    starts.append(((startx,-1),(0,1)))
    starts.append(((startx,len(grid)),(0,-1)))

m = 0
for start in starts:
    energized = set()
    frontier = set([start])
    visited = set()
    while frontier:
        (x,y),(dx,dy) = frontier.pop()
        if (x,y) != start[0]:
            visited.add(((x,y),(dx,dy)))
            energized.add((x,y))
        
        newx,newy = x+dx,y+dy
        if not 0 <= newx < len(grid[0]): continue
        if not 0 <= newy < len(grid): continue
        c = grid[newy][newx]
        for newdx,newdy in dirs[c][(dx,dy)]:
            if ((newx,newy),(newdx,newdy)) in visited: continue
            frontier.add(((newx,newy),(newdx,newdy)))
    m = max(m, len(energized))
print(m)