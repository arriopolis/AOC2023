import sys
import itertools as it

adjacent = {
    '.' : set(),
    '-' : set([(-1,0), (1,0)]),
    '|' : set([(0,1), (0,-1)]),
    'L' : set([(0,-1), (1,0)]),
    'J' : set([(-1,0), (0,-1)]),
    'F' : set([(0,1), (1,0)]),
    '7' : set([(-1,0), (0,1)]),
    'S' : set([(-1,0), (0,1), (0,-1), (1,0)])
}

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

start = None
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c == 'S':
            start = (x,y)
            break
    else: continue
    break

cur_squares = set([start])
visited_squares = set()
loop_complete = False
ctr = 0
while True:
    ctr += 1
    visited_squares.update(cur_squares)
    new_cur_squares = set()
    for x,y in cur_squares:
        for dx,dy in adjacent[grid[y][x]]:
            newx,newy = x+dx,y+dy
            if newx < 0 or newx >= len(grid[0]): continue
            if newy < 0 or newy >= len(grid): continue

            if (newx,newy) in visited_squares: continue
            offset = (-dx,-dy)
            if offset in adjacent[grid[newy][newx]]:
                new_cur_squares.add((newx,newy))
    if len(new_cur_squares) == 1: break
    cur_squares = new_cur_squares
print(ctr)