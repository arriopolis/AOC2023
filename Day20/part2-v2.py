import sys
import queue

mods = {}
for line in sys.stdin:
    src,dests = line.strip().split(' -> ')
    if src[0] in '&%':
        mode = src[0]
        src = src[1:]
    else: mode = ''
    mods[src] = (mode, dests.split(', '))

groups = [
    ['hd', 'lt', 'rh', 'gx', 'xf', 'tg', 'ks', 'tc', 'qz', 'rl', 'pf', 'pr', 'nl', 'cq'], #hd, lt, gx, xf, ks, tc --> 0, 1, 3, 4, 6, 7
    ['sq', 'vh', 'qc', 'gp', 'cp', 'jt', 'kb', 'hj', 'cf', 'jg', 'pd', 'mt', 'rr', 'rv'], #sq, qc, gp, jt         --> 0, 2, 3, 5
    ['jz', 'ht', 'jv', 'zs', 'dq', 'jc', 'xv', 'dx', 'fq', 'xz', 'zp', 'mm', 'dj', 'dc'], #jz, ht, zs, jc, fq     --> 0, 1, 3, 5, 8
    ['zj', 'kn', 'xn', 'gf', 'gv', 'vr', 'qb', 'hq', 'nx', 'bs', 'rd', 'vs', 'pb', 'vp']  #zj, gf, gv, vr, qb, hq --> 0, 3, 4, 5, 6, 7
]

res = 1
for g in groups:
    states = {src : False for src,(mode,_) in mods.items() if mode == '%'}
    signals = {src : {} for src,(mode,_) in mods.items() if mode == '&'}
    for src,(mode,dests) in mods.items():
        for dest in dests:
            if dest in mods and mods[dest][0] == '&':
                signals[dest][src] = False

    pulses = queue.Queue()
    ctr = 0
    while True:
        if ctr > 0 and not any(states.values()): break
        ctr += 1
        pulses.put((g[0], False))
        while not pulses.empty():
            mod, pulse = pulses.get()
            if mod in mods and mods[mod][0] == '&':
                new_pulse = not all(signals[mod].values())
                for dest in mods[mod][1]:
                    pulses.put((dest, new_pulse))
                    if dest in signals: signals[dest][mod] = new_pulse
            elif mod in mods and mods[mod][0] == '%' and not pulse:
                states[mod] = not states[mod]
                for dest in mods[mod][1]:
                    pulses.put((dest, states[mod]))
                    if dest in signals: signals[dest][mod] = states[mod]
    res *= ctr
print(res)