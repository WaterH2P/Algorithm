# 时间分隔
for t in range(int(input())):
    n, in_shed, out_shed = int(input()), list(map(int, input().split())), list(map(int, input().split()))
    arr = []
    for it in in_shed:
        arr.append((it, 1))
    for it in out_shed:
        arr.append((it, 0))
    arr.sort(key=lambda i: i[0])
    maxi, cur = 0, 0
    for it in arr:
        if it[1]:
            cur += 1
            maxi = max(maxi, cur)
        else:
            cur -= 1
    print(maxi)