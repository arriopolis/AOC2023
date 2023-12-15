import sys

for line in sys.stdin:
    s = line.strip()

t = 0
for x in s.split(','):
    cur = 0
    for c in x:
        cur = ((cur + ord(c)) * 17) % 256
    t += cur
print(t)