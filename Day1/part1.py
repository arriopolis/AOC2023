import sys

s = 0
for line in sys.stdin:
    first_digit = -1
    last_digit = -1
    for c in line:
        if c in '0123456789':
            if first_digit == -1:
                first_digit = int(c)
            last_digit = int(c)
    num = 10*first_digit + last_digit
    s += num
print(s)