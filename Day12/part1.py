import sys
import itertools as it

total = 0
for line in sys.stdin:
    pattern, group = line.strip().split()
    group = list(map(int, group.split(',')))

    num_questions = pattern.count('?')
    num_hashes = pattern.count('#')
    tot_hashes = sum(group)
    
    tot_ctr = 0
    for s in it.combinations(range(num_questions), tot_hashes - num_hashes):
        newp = []
        ctr = 0
        for c in pattern:
            if c == '?':
                if ctr in s:
                    newp.append('#')
                else:
                    newp.append('.')
                ctr += 1
            else:
                newp.append(c)
        
        lastc = '.'
        ctr = 0
        newg = []
        for c in newp:
            if c == '#':
                ctr += 1
            elif lastc == '#':
                newg.append(ctr)
                ctr = 0
            lastc = c
        if lastc == '#': newg.append(ctr)

        if group == newg: tot_ctr += 1
    
    total += tot_ctr    
print(total)