import sys

order = 'AKQT98765432J'
relabel = {c : chr(ord('A')+j) for j,c in enumerate(order)}

hands = []
for line in sys.stdin:
    hand, bid = line.strip().split()

    ctrs = {}
    jokers = 0
    for c in hand:
        if c == 'J':
            jokers += 1
            continue
        if c not in ctrs: ctrs[c] = 0
        ctrs[c] -= 1
    t = list(sorted(ctrs.values()))
    if len(t) == 0: t = [-5]
    else: t[0] -= jokers
    hands.append((tuple(t), ''.join(relabel[c] for c in hand), int(bid)))

hands.sort(reverse = True)
s = 0
for j,(_,_,b) in enumerate(hands):
    s += (j+1)*b
print(s)