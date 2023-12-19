import sys

wfs = {}
t = 0
for line in sys.stdin:
    if not line.strip(): continue
    if not line.startswith('{'):
        wf, rules = line.strip()[:-1].split('{')
        wfs[wf] = []
        for rule in rules.split(','):
            (condition, result) = rule.split(':') if ':' in rule else ('True', rule)
            wfs[wf].append((condition, result))
    else:
        for expr in line.strip()[1:-1].split(','):
            exec(expr)
        
        wf = 'in'
        while wf in wfs:
            for condition, result in wfs[wf]:
                if eval(condition):
                    wf = result
                    break
        if wf == 'A':
            t += x+m+a+s
print(t)