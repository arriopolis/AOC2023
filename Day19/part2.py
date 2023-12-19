import sys

wfs = {}
for line in sys.stdin:
    if not line.strip(): break
    if not line.startswith('{'):
        wf, rules = line.strip()[:-1].split('{')
        wfs[wf] = []
        for rule in rules.split(','):
            (condition, result) = rule.split(':') if ':' in rule else ('', rule)
            wfs[wf].append((condition, result))

def count_arrangements(wf, intervals):
    if any(l > u for l,u in intervals.values()): return 0

    if wf == 'R': return 0
    if wf == 'A':
        prod = 1
        for l,u in intervals.values():
            prod *= u-l+1
        return prod
    
    t = 0
    for condition, result in wfs[wf]:
        if not condition:
            t += count_arrangements(result, intervals)
            break
        
        c = condition[0]
        n = int(condition[2:])

        new_intervals = intervals.copy()
        if condition[1] == '<':
            new_intervals[c] = (intervals[c][0], n-1)
            intervals[c] = (n, intervals[c][1])
        else:
            new_intervals[c] = (n+1, intervals[c][1])
            intervals[c] = (intervals[c][0], n)
        t += count_arrangements(result, new_intervals)
    return t

print(count_arrangements('in', {c : (1,4000) for c in 'xmas'}))