import sys
import heapq

bricks = []
for line in sys.stdin:
    (x1,y1,z1),(x2,y2,z2) = map(lambda x : map(int,x.split(',')), line.strip().split('~'))
    bricks.append(((x1,y1,z1),(x2,y2,z2)))

bricks.sort(key = lambda x : min(p[2] for p in x))

fallen_bricks = []
supports = {}
for (x1,y1,z1),(x2,y2,z2) in bricks:
    xmin1,xmax1 = min(x1,x2),max(x1,x2)
    ymin1,ymax1 = min(y1,y2),max(y1,y2)
    z = 1
    s = set()
    
    for (x3,y3,z3),(x4,y4,z4) in reversed(fallen_bricks):
        xmin2,xmax2 = min(x3,x4),max(x3,x4)
        ymin2,ymax2 = min(y3,y4),max(y3,y4)
        zmax2 = max(z3,z4)

        if xmax2 < xmin1 or xmax1 < xmin2: continue
        if ymax2 < ymin1 or ymax1 < ymin2: continue

        if zmax2 + 1 == z:
            s.add(((x3,y3,z3),(x4,y4,z4)))
        elif zmax2 + 1 > z:
            s = set([((x3,y3,z3),(x4,y4,z4))])
            z = zmax2 + 1
    
    fallen_bricks.append(((x1,y1,z),(x2,y2,z+abs(z1-z2))))
    supports[((x1,y1,z),(x2,y2,z+abs(z1-z2)))] = s

essential = set()
for s in supports.values():
    if len(s) == 1:
        essential.update(s)

supp = {a : set() for a in supports}
for a,bs in supports.items():
    for b in bs:
        supp[b].add(a)

t = 0
for a in essential:
    to_fall = set([a])
    q = [(min(p[2] for p in a),a)]
    while q:
        _,a = heapq.heappop(q)
        for b in supp[a]:
            if supports[b] <= to_fall:
                to_fall.add(b)
                heapq.heappush(q, (min(p[2] for p in b), b))
    t += len(to_fall)-1

# to_fall = {a : set() for a in supports}
# while supp:
#     todel = set()
#     for a,bs in supp.items():
#         if not bs: todel.add(a)
#     for a in todel:
#         for b in supports[a]:
#             to_fall[b].update(to_fall[a])
#             to_fall[b].add(a)
#             supp[b].remove(a)
#         del supp[a]

# t = 0
# ctr = 0
# for a in essential:
#     ctr += 1
#     t += len(to_fall[a])
print(t)