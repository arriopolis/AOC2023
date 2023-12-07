import sys

order = 'AKQJT98765432'
relabel = {c : chr(ord('A')+j) for j,c in enumerate(order)}

hands = []
for line in sys.stdin:
    hand, bid = line.strip().split()

    ctrs = {}
    for c in hand:
        if c not in ctrs: ctrs[c] = 0
        ctrs[c] -= 1
    t = tuple(sorted(ctrs.values()))
    hands.append((t, ''.join(relabel[c] for c in hand), int(bid)))

hands.sort(reverse = True)
s = 0
for j,(_,_,b) in enumerate(hands):
    s += (j+1)*b
print(s)