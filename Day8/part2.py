import sys
from math import gcd, lcm

def egcd(a,b):
    if a == 0: return b,0,1
    g,x1,y1 = egcd(b%a,a)
    x = y1 - (b//a) * x1
    y = x1
    return g,x,y

pattern = None
instrs = {}
for line in sys.stdin:
    if not line.strip(): continue
    if pattern is None:
        pattern = line.strip()
        continue
    
    src, dests = line.strip().split(' = ')
    instrs[src] = tuple(dests.lstrip('(').rstrip(')').split(', '))

res = 1
for x in instrs:
    if not x.endswith('A'): continue
    
    visited = {}
    marked = []
    
    pos = x
    ctr = 0
    while (pos, ctr%len(pattern)) not in visited:
        visited[(pos, ctr%len(pattern))] = ctr
        if pos.endswith('Z'): marked.append(ctr)

        instr = pattern[ctr%len(pattern)]
        j = 1 if instr == 'R' else 0
        pos = instrs[pos][j]
        ctr += 1
    
    period = ctr - visited[(pos, ctr%len(pattern))]

    assert len(marked) == 1
    marked = marked[0]
    assert marked == period
    res = lcm(res, period)
print(res)