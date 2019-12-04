import sys
for line in sys.stdin:
    n, *arr = list(map(int, line.split()))
    maximum = max(arr)
    bucket = [0] * (maximum + 1)
    for val in arr:
        bucket[val] += 1
    res = []
    for idx, val in enumerate(bucket):
        for _ in range(val):
            res.append(idx)
    print(*res)
