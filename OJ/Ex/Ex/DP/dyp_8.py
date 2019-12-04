for _ in range(int(input().strip())):
    r, c = map(int, input().strip().split())
    valuesT = list(map(int, input().strip().split()))
    values = [[0 for j in range(c)] for i in range(r)]
    for x in range(r):
        for y in range(c):
            values[x][y] = valuesT[x * c + y]
    dp = [[0 for j in range(c)] for i in range(r)]
    dp2 = [[0 for j in range(c)] for i in range(r)]
    dp[0][0] = values[0][0]
    dp2[0][0] = values[0][0]
    for x in range(r):
        for y in range(c):
            if x == 0 and y == 0:
                continue
            if x == 0:
                dp[x][y] = dp[x][y-1] + values[x][y]
                dp2[x][y] = min(dp[x][y], dp[x][y-1])
            elif y == 0:
                dp[x][y] = dp[x-1][y] + values[x][y]
                dp2[x][y] = min(dp[x][y], dp[x-1][y])
            else:
                if dp2[x][y-1] >= dp2[x-1][y]:
                    dp[x][y] = dp[x][y-1] + values[x][y]
                    dp2[x][y] = min(dp[x][y], dp2[x][y-1])
                else:
                    dp[x][y] = dp[x-1][y] + values[x][y]
                    dp2[x][y] = min(dp[x][y], dp2[x-1][y])
    print(abs(dp2[-1][-1]) + 1 if dp2[-1][-1] < 1 else 0)