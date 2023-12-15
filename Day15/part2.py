import sys

for line in sys.stdin:
    s = line.strip()

boxes = [[] for _ in range(256)]
for x in s.split(','):
    box = 0
    for c in x:
        if c in ('=','-'): break
        box = ((box + ord(c)) * 17) % 256
    
    if c == '=':
        newl,newf = x.split('=')
        for j,(l,f) in enumerate(boxes[box]):
            if l == newl:
                boxes[box][j] = (newl,int(newf))
                break
        else: boxes[box].append((newl,int(newf)))
    elif c == '-':
        newl = x.split('-')[0]
        for j,(l,f) in enumerate(boxes[box]):
            if l == newl:
                del boxes[box][j]
                break

t = 0
for box,lenses in enumerate(boxes):
    for j,(l,f) in enumerate(lenses):
        t += (box+1) * (j+1) * f
print(t)