# 是否能通过考试
for t in range(int(input())):
    n, h, p = map(int, input().split())
    qs = []
    for _ in range(n):
        qs.append(tuple(map(int, input().split())))
    dp = [[0] * (h+1) for i in range(n+1)]
    mini = h
    for i in range(1, n+1):
        for j in range(1, h+1):
            if qs[i-1][0] < j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-qs[i-1][0]]+qs[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][j] >= p:
                mini = min(mini, j-1)
    if dp[-1][-1] < p:
        print('NO')
    else:
        print('YES', mini)