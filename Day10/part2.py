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
left_loop = [start]
right_loop = [start]
while cur_squares:
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
                if left_loop[-1] == (x,y):
                    left_loop.append((newx,newy))
                elif right_loop[-1] == (x,y):
                    right_loop.append((newx,newy))
                new_cur_squares.add((newx,newy))
    cur_squares = new_cur_squares

loop = left_loop + right_loop[-2:0:-1]

_,j = min((x,j) for j,(x,_) in enumerate(loop))
loop = loop[j:] + loop[:j]
if loop[-1][1] == loop[0][1]: loop = loop[::-1]

intervals = {}
startidx = 0
for j,(x,y) in enumerate(loop):
    newy = loop[(j+1)%len(loop)][1]
    if newy == y: continue

    oldy = loop[(startidx-1)%len(loop)][1]
    startx = loop[startidx][0]
    intx = tuple(sorted([startx, x]))
    if y not in intervals: intervals[y] = []
    intervals[y].append((intx, oldy != newy))

    startidx = (j+1)%len(loop)

ctr = 0
for y,intvs in intervals.items():
    intvs.sort()
    inside = False
    for ((xs1,xe1),c1),((xs2,xe2),c2) in zip(intvs[:-1], intvs[1:]):
        if c1: inside = not inside
        if inside: ctr += xs2 - xe1 - 1
print(ctr)