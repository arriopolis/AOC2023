import sys

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

s = 0
for line in sys.stdin:
    first_digit = -1
    last_digit = -1
    for j,c in enumerate(line):
        digit = -1
        for n,ls in enumerate(nums):
            if line[j:j+len(ls)] == ls:
                digit = n+1
                break
        else:
            if c in '0123456789':
                digit = int(c)
        if digit == -1: continue

        if first_digit == -1:
            first_digit = digit
        last_digit = digit
    num = 10*first_digit + last_digit
    s += num
print(s)