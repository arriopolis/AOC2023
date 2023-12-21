import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c == 'S':
            startx,starty = x,y

frontier = set([(startx,starty)])
for _ in range(64):
    new_frontier = set()
    for x,y in frontier:
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            newx,newy = x+dx,y+dy
            if not 0 <= newx < len(grid[0]): continue
            if not 0 <= newy < len(grid): continue
            if grid[newy][newx] == '#': continue
            new_frontier.add((newx,newy))
    frontier = new_frontier
print(len(frontier))