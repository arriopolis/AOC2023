import sys

s = 0
for line in sys.stdin:
    data = line.strip().split(':')[1].strip()
    winning_part, available_part = data.split('|')
    winning_numbers = list(map(int,winning_part.strip().split()))
    available_numbers = list(map(int,available_part.strip().split()))
    ctr = 0
    for n in available_numbers:
        if n in winning_numbers:
            ctr += 1
    if ctr > 0:
        s += 2**(ctr-1)
print(s)