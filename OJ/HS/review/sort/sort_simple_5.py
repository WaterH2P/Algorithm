# TODO
import sys
for line in sys.stdin:
    n, *arr = list(map(int, line.split()))
    s = list()
    l, r = 0, n-1
    s.append(l)
    s.append(r)
    while len(s):
        r = s.pop()
        l = s.pop()
        if r > l:
            m = (l+r)//2


