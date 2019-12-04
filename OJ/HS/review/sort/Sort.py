for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    cnt = dict.fromkeys(arr, 0)
    for val in arr:
        cnt[val] += 1
    tups = list(cnt.items())
    tups.sort(key=lambda tup: (-tup[1], tup[0]))
    res = []
    for tup in tups:
        for i in range(tup[1]):
            res.append(tup[0])
    print(*res)