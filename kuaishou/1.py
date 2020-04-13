bds = input().strip()
lr, l, r = 0, 0, 0
stack = 0
for s in bds:
    if s == '(': stack += 1
    elif s == ')':
        if stack == 0: r += 1
        elif stack > 0:
            stack -= 1
            lr += 1
l = stack
print(lr, l, r)