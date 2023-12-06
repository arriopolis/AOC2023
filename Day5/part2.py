import sys

seed_ranges = None
maps = {}
current_map = None
for line in sys.stdin:
    if not line.strip(): continue
    elif line.strip().startswith('seeds:'):
        nums = list(map(int,line.strip().split(':')[1].split()))
        seed_ranges = list(zip(nums[::2], nums[1::2]))
    elif line.strip().endswith('map:'):
        start,end = line.strip().split()[0].split('-to-')
        maps[start] = (end, [])
        current_map = start
    else:
        d,s,l = map(int, line.strip().split())
        maps[start][1].append((d,s,l))

m = float('inf')
mode = 'seed'
ranges = seed_ranges
while mode != 'location':
    mode, mapping = maps[mode]
    new_ranges = []
    for d,s,l in mapping:
        old_ranges = []
        for rs,rl in ranges:
            news = max(rs,s)
            newl = min(s+l,rs+rl)-news
            if newl > 0: new_ranges.append((news+d-s,newl))
            if rs < s:
                old_ranges.append((rs,min(rl,s-rs)))
            if s+l < rs+rl:
                olds = max(s+l,rs)
                old_ranges.append((olds, rs+rl-olds))
        ranges = old_ranges
    ranges.extend(new_ranges)
print(min(s for s,l in ranges))