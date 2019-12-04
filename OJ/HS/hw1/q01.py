# Author		: tsnk
# Created		: 2019/9/16
# Last Modified	: 2019/9/16

import sys

i = int(input())
for line in sys.stdin:
    arr = list(map(int, line.split()))
    res = 0
    for num in arr[1:]:
        res += num
    print(res)
    i -= 1
    if i > 0:
        print()
