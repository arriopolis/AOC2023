import sys
import itertools as it

# xmin,xmax = 7,27
# ymin,ymax = 7,27

xmin,xmax = 200000000000000,400000000000000
ymin,ymax = 200000000000000,400000000000000

stones = []
for line in sys.stdin:
    (x,y,z),(vx,vy,vz) = map(lambda x : map(int,x.split(', ')), line.strip().split(' @ '))
    stones.append(((x,y,z),(vx,vy,vz)))

ctr = 0
for ((x1,y1,_),(vx1,vy1,_)),((x2,y2,_),(vx2,vy2,_)) in it.combinations(stones, 2):
    # x = x1 + t*vx1 = x2 + s*vx2
    # y = y1 + t*vy1 = y2 + s*vy2

    # vy1*x = vy1*x1 + t*vx1*vy1
    # vx1*y = vx1*y1 + t*vx1*vy1
    
    # vy1*x - vx1*y = vy1*x1 - vx1*y1
    # vy2*x - vx2*y = vy2*x2 - vx2*y2

    # vx2*vy1*x - vx2*vx1*y = vx2*vy1*x1 - vx2*vx1*y1
    # vx1*vy2*x - vx1*vx2*y = vx1*vy2*x2 - vx1*vx2*y2

    # (vx2*vy1 - vx1*vy2)*x = vx2*vy1*x1 - vx2*vx1*y1 - vx1*vy2*x2 + vx1*vx2*y2

    a = vx2*vy1 - vx1*vy2
    b = vx2*vy1*x1 - vx2*vx1*y1 - vx1*vy2*x2 + vx1*vx2*y2
    if (a*xmin-b) * (a*xmax-b) > 0: continue

    # vy2*vy1*x - vy2*vx1*y = vy2*vy1*x1 - vy2*vx1*y1
    # vy1*vy2*x - vy1*vx2*y = vy1*vy2*x2 - vy1*vx2*y2

    # (vy1*vx2 - vy2*vx1)*y = vy2*vy1*x1 - vy2*vx1*y1 - vy1*vy2*x2 + vy1*vx2*y2

    c = vy1*vx2 - vy2*vx1
    d = vy2*vy1*x1 - vy2*vx1*y1 - vy1*vy2*x2 + vy1*vx2*y2
    if (c*ymin-d) * (c*ymax-d) > 0: continue
    
    # x = x1 + t*vx1
    # t*vx1*a = b - x1*a
    if (b - x1*a) * (vx1 * a) < 0: continue
    if (d - y1*c) * (vy1 * c) < 0: continue

    # x = x2 + s*vx2
    # s*vx2*a = b - a*x2
    if (b - x2*a) * (vx2 * a) < 0: continue
    if (d - y2*c) * (vy2 * c) < 0: continue
    
    # print(((x1,y1),(vx1,vy1)),((x2,y2),(vx2,vy2)))
    # print(b/a, d/c)

    ctr += 1
print(ctr)