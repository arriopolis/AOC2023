import sys

t = 0
for line in sys.stdin:
    l = list(map(int, line.strip().split()))
    
    hist = [l]
    while any(c != 0 for c in l):
        l = [r-l for l,r in zip(l[:-1], l[1:])]
        hist.append(l)
    
    x = 0
    for l in hist[::-1]:
        x = l[0] - x
    t += x
print(t)