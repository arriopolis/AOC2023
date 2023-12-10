import sys

t = 0
for line in sys.stdin:
    l = list(map(int, line.strip().split()))
    
    s = 0
    while any(c != 0 for c in l):
        s += l[-1]
        l = [r-l for l,r in zip(l[:-1], l[1:])]
    t += s
print(t)