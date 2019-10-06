import sys
str = sys.stdin.readline().split()
while str:
    sum = 0
    i = 1
    while i < len(str):
        sum += int(str[i])
        i += 1
    print( sum )
    str = sys.stdin.readline().split()