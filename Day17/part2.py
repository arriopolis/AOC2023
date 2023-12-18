import sys
import heapq

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

q = [(0,0,0,None)]
visited = set()
while q:
    d,x,y,hist = heapq.heappop(q)
    if (x,y) == (len(grid[0])-1, len(grid)-1):
        print(d)
        sys.exit()

    if (x,y,hist) in visited: continue
    visited.add((x,y,hist))
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        newx,newy = x+dx,y+dy
        if not 0 <= newx < len(grid[0]): continue
        if not 0 <= newy < len(grid): continue
        if hist is not None:
            olddx,olddy,n = hist
            if (dx,dy) == (-olddx,-olddy): continue
            if (olddx,olddy) == (dx,dy):
                newn = n+1
                if newn > 10: continue
            else:
                if n < 4: continue
                newn = 1
            newhist = (dx,dy,newn)
        else: newhist = (dx,dy,1)
        
        newd = d + grid[newy][newx]
        heapq.heappush(q, (newd, newx, newy, newhist))