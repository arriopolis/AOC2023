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

energized = set()
frontier = set([((-1,0),(1,0))])
visited = set()
while frontier:
    (x,y),(dx,dy) = frontier.pop()
    if (x,y) != (-1,0):
        visited.add(((x,y),(dx,dy)))
        energized.add((x,y))
    
    newx,newy = x+dx,y+dy
    if not 0 <= newx < len(grid[0]): continue
    if not 0 <= newy < len(grid): continue
    c = grid[newy][newx]
    for newdx,newdy in dirs[c][(dx,dy)]:
        if ((newx,newy),(newdx,newdy)) in visited: continue
        frontier.add(((newx,newy),(newdx,newdy)))
print(len(energized))