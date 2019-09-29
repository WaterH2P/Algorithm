import sys
count = int(sys.stdin.readline())
i = 0
while i < count:
    str = sys.stdin.readline().split()
    sum = 0
    j = 1
    while j < len(str):
        sum += int(str[j])
        j += 1
    print( sum )
    i += 1