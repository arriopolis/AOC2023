import sys
import itertools as it

# Store the results we have already computed
dct = {}

def count_assignments(p, g):
    # Check if there are immediate problems
    if sum(g) + len(g) - 1 > len(p): return 0
    num_hashes = p.count('#')
    num_questions = p.count('?')
    if not num_hashes <= sum(g) <= num_hashes + num_questions: return 0

    # If there are no more groups to assign, stop
    if not g: return 1

    # Check if we have already computed it
    if (tuple(p),tuple(g)) in dct: return dct[(tuple(p),tuple(g))]

    # Find the middle group to assign
    k = len(g)//2
    l = g[k]
    t = 0
    for j in range(len(p)):
        
        # Check if it fits at position j
        if j+l > len(p): continue
        if any(c == '.' for c in p[j:j+l]): continue
        if j > 0 and p[j-1] == '#': continue
        if j+l < len(p) and p[j+l] == '#': continue

        # Count the assignments on both sides
        left = count_assignments((p[:j-1] if j > 0 else []), g[:k])
        right = count_assignments(p[j+l+1:], g[k+1:])
        t += left * right
    
    # Store the result
    dct[(tuple(p),tuple(g))] = t
    return t

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