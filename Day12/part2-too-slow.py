import sys
import itertools as it

def count_assignments(p, g):
    for j,c in enumerate(p):
        if c == '#':
            # Check if a group fits here
            if not g: return 0
            if j+g[0] > len(p): return 0
            if any(c2 == '.' for c2 in p[j:j+g[0]]): return 0
            if j+g[0] < len(p) and p[j+g[0]] == '#': return 0
            
            # The group fits
            return count_assignments(p[j+g[0]+1:], g[1:])
        elif c == '?':
            return count_assignments(['#'] + p[j+1:], g) + count_assignments(p[j+1:], g)
    return 1 if not g else 0

total = 0
for j,line in enumerate(sys.stdin):
    pattern, group = line.strip().split()
    group = list(map(int, group.split(',')))

    pattern = list('?'.join([pattern]*5))
    group *= 5

    print(''.join(pattern), group)
    t = count_assignments(pattern, group)
    print(t)
    total += t
print(total)