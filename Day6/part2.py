import sys
from math import sqrt, floor, ceil

for line in sys.stdin:
    if line.strip().startswith('Time:'):
        data = line.strip().split(':')[1].strip()
        data = data.replace(' ','')
        ms = int(data)
    if line.strip().startswith('Distance:'):
        data = line.strip().split(':')[1].strip()
        data = data.replace(' ','')
        d = int(data)

print(ms,d)

ctr = 0

# The equation is t**2 - ms*t + dist = 0
D = ms**2 - 4*d
tmin = (ms - sqrt(D))/2
tmax = (ms + sqrt(D))/2
print(floor(tmax) - ceil(tmin) + 1)