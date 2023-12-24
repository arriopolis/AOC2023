import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

g = {}
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c != '#':
            neighbors = {}
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                newx,newy = x+dx,y+dy
                if not 0 <= newx < len(grid[0]): continue
                if not 0 <= newy < len(grid): continue
                if grid[newy][newx] != '#':
                    neighbors[(newx,newy)] = 1
            g[(x,y)] = neighbors

for p in list(g.keys()):
    if len(g[p]) == 2:
        (p1,d1),(p2,d2) = g[p].items()
        g[p1].pop(p)
        g[p2].pop(p)
        g[p1][p2] = d1 + d2
        g[p2][p1] = d1 + d2
        g.pop(p)

hist = {}
def DFS(cur, visited = None):
    if cur == (len(grid[0])-2, len(grid)-1): return 0
    if visited is None: visited = set()

    k = (cur, tuple(sorted(visited)))
    if k in hist: return hist[k]
    
    m = -float('inf')
    for j,(n,d) in enumerate(g[cur].items()):
        if n in visited: continue
        m = max(m, d + DFS(n, visited.union(set([cur]))))
    hist[k] = m
    return m

res = DFS((1,0))
print(res)