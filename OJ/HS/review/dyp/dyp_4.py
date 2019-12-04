# 如何花最少的钱购买蔬菜
for t in range(int(input())):
    n = int(input())
    a = [tuple(map(int, input().split())) for i in range(n)]
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][:] = a[0][:]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(
                    dp[i - 1][(j + 1) % 3],
                    dp[i - 1][(j + 2) % 3]
                ) + a[i][j]
    print(min(dp[-1]))