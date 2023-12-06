import sys

ctrs = []
for line in sys.stdin:
    data = line.strip().split(':')[1].strip()
    winning_part, available_part = data.split('|')
    winning_numbers = list(map(int,winning_part.strip().split()))
    available_numbers = list(map(int,available_part.strip().split()))
    ctr = 0
    for n in available_numbers:
        if n in winning_numbers:
            ctr += 1
    ctrs.append(ctr)

copies = [1]*len(ctrs)
for j,ctr in enumerate(ctrs):
    m = copies[j]
    if ctr > 0:
        for k in range(j+1,j+ctr+1):
            copies[k] += m
print(sum(copies))