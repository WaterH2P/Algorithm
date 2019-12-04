from itertools import combinations

u = int(input())
while u > 0:
    u -= 1
    arr = list(map(int, input().split()))
    n = len(arr)
    idx_list = range(n)
    raw_res = list()
    for i in range(1, n+1):
        for com in combinations(idx_list, i):
            tmp = list()
            for idx in com:
                tmp.append(arr[idx])
            correct = True
            inc = True
            j = 0
            while j < len(tmp)-1:
                if tmp[j] > tmp[j+1]:
                    inc = False
                if tmp[j] < tmp[j+1] and inc is False:
                    correct = False
                    break
                j += 1
            if correct:
                raw_res.append(tmp)
    distinct_res = [list(t) for t in set(tuple(_) for _ in raw_res)]
    lens = list()
    for line in distinct_res:
        lens.append(len(line))
    max_len = max(lens)
    res = list()
    for index, line in enumerate(distinct_res):
        if lens[index] == max_len:
            res.append(line)
    res.sort()
    for line in res:
        print(*line)

