# 美团 2020 春招笔试第四题
import sys

n, m, k = list(map(int, input().strip().split()))
ais = [int(_) for _ in input().strip().split()]
info = [[None, {}] for i in range(n)]
for i in range(n):
    info[i][0] = ais[i]
    info[i][1][ais[i]] = 0
roads = [[] for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().strip().split()))
    u, v = u - 1, v - 1
    if v not in roads[u]:
        roads[u].append(v)
    if u not in roads[v]:
        roads[v].append(u)
isChange = True
while isChange:
    isChange = False
    for i in range(n):
        for v in roads[i]:
            if info[v][0] not in info[i][1] or 1 < info[i][1][info[v][0]]:
                info[i][1][info[v][0]] = 1
                isChange = True
            for ai in info[v][1]:
                if ai not in info[i][1] or info[v][1][ai] + 1 < info[i][1][ai]:
                    info[i][1][ai] = info[v][1][ai] + 1
                    isChange = True
totals = []
for i in range(n):
    total = 0
    for ai in info[i][1]:
        total += info[i][1][ai]
    totals.append(str(total))
output = ' '.join(totals) + '\n'
sys.stdout.write(output)