import sys

pattern = None
instrs = {}
for line in sys.stdin:
    if not line.strip(): continue
    if pattern is None:
        pattern = line.strip()
        continue
    
    src, dests = line.strip().split(' = ')
    instrs[src] = tuple(dests.lstrip('(').rstrip(')').split(', '))

pos = 'AAA'
ctr = 0
while pos != 'ZZZ':
    instr = pattern[ctr%len(pattern)]
    j = 1 if instr == 'R' else 0
    pos = instrs[pos][j]
    ctr += 1
print(ctr)