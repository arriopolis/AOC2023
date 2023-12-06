import sys

UB = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

s = 0
for line in sys.stdin:
    game_id = int(line.strip().split()[1].rstrip(':'))
    
    data = line.strip().split(':')[1].strip()
    for obs in data.split(';'):
        for x in obs.split(','):
            n,c = x.split()
            n = int(n)
            if c in UB and n > UB[c]:
                break
        else: continue
        break
    else:
        s += game_id
print(s)