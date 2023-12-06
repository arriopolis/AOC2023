import sys

COLORS = ['red', 'green', 'blue']

s = 0
for line in sys.stdin:
    game_id = int(line.strip().split()[1].rstrip(':'))
    
    LB = {c : 0 for c in COLORS}
    data = line.strip().split(':')[1].strip()
    for obs in data.split(';'):
        for x in obs.split(','):
            n,c = x.split()
            n = int(n)
            if c in LB:
                LB[c] = max(LB[c],n)
    power = 1
    for c in COLORS:
        power *= LB[c]
    s += power
print(s)