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

states = {src : False for src,(mode,_) in mods.items() if mode == '%'}
signals = {src : {} for src,(mode,_) in mods.items() if mode == '&'}
for src,(mode,dests) in mods.items():
    for dest in dests:
        if dest in mods and mods[dest][0] == '&':
            signals[dest][src] = False

pulses = queue.Queue()
ctr = 0
while True:
    ctr += 1
    print(ctr, end = '\r')
    pulses.put(('broadcaster', False))
    while not pulses.empty():
        mod, pulse = pulses.get()

        if mod == 'rx' and not pulse:
            print(ctr)
            sys.exit()
        
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
        elif mod == 'broadcaster':
            for dest in mods[mod][1]:
                pulses.put((dest, pulse))
                if dest in signals: signals[dest][mod] = pulse