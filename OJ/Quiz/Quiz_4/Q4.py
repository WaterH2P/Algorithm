for z1 in range(int(input().strip())):
    sellers = []
    n = int(input().strip())
    for z2 in range(n):
        sellers.append(list(map(int, input().strip().split(' '))))
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][0] = sellers[0][0]
    dp[0][1] = sellers[0][1]
    dp[0][2] = sellers[0][2]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + sellers[i][j]
    print(dp)
    answer = 10 ** 9
    for i in range(3):
        answer = min(answer, dp[n - 1][i])
    print(answer)