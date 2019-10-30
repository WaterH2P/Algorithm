import sys
str = sys.stdin.readline().split()
while int(str[0]) > 0:
    if len(str) == 1:
        break
    sum = 0
    i = 1
    while i < len(str):
        sum += int(str[i])
        i += 1
    print( sum )
    str = sys.stdin.readline().split()