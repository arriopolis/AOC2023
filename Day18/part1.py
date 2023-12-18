import sys

dirs = {
    'R' : (1,0),
    'U' : (0,-1),
    'D' : (0,1),
    'L' : (-1,0)
}

instrs = []
for line in sys.stdin:
    dir, n, color = line.strip().split()
    instrs.append((dir, int(n), color[2:-1])) 

x,y = 0,0
polygon = []
c = 0
for dir,n,_ in instrs:
    dx,dy = dirs[dir]
    x += n*dx
    y += n*dy
    c += n
    polygon.append((x,y))

t = 0
for (x1,y1),(x2,y2) in zip(polygon, polygon[1:] + [polygon[0]]):
    t += y2*x1 - y1*x2
t //= 2
t += c//2
t += 1
print(t)