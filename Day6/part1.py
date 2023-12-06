import sys

for line in sys.stdin:
    if line.strip().startswith('Time:'):
        data = line.strip().split(':')[1].strip()
        mss = list(map(int, data.split()))
    if line.strip().startswith('Distance:'):
        data = line.strip().split(':')[1].strip()
        ds = list(map(int, data.split()))

prod = 1
for ms,d in zip(mss, ds):
    ctr = 0
    for t in range(0,ms+1):
        dist = (ms-t)*t
        if dist > d: ctr += 1
    prod *= ctr
print(prod)