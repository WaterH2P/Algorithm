import sys
for line in sys.stdin:
    print(*sorted(list(map(int, line.split()))[1:]))



