import sys

seeds = None
maps = {}
current_map = None
for line in sys.stdin:
    if not line.strip(): continue
    elif line.strip().startswith('seeds:'):
        seeds = set(map(int,line.strip().split(':')[1].split()))
    elif line.strip().endswith('map:'):
        start,end = line.strip().split()[0].split('-to-')
        maps[start] = (end, [])
        current_map = start
    else:
        d,s,l = map(int, line.strip().split())
        maps[start][1].append((d,s,l))

m = float('inf')
for num in seeds:
    mode = 'seed'
    while mode != 'location':
        mode, mapping = maps[mode]
        for d,s,l in mapping:
            if s <= num < s+l:
                num += (d-s)
                break
    m = min(m, num)
print(m)