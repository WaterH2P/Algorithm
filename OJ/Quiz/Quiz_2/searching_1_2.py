n = int(input().strip())
for t in range(n):
    numP, numB = map(int, input().split())
    boards = list(map(int, input().split()))
    dp = [[0 for i in range(numB + 1)] for j in range(numP + 1)]
    for i in range(1, numB + 1) :
        dp[1][i] = sum(boards[0:i])
    for i in range(1, numP + 1) :
        dp[i][1] = boards[0]
    for i in range(2, numP + 1) :
        for j in range(2, numB + 1) :
            maxT = 9999
            for k in range(1, j + 1) :
                maxT = min(maxT, max(dp[i - 1][k], sum(boards[k:j])))
                dp[i][j] = maxT
    print(dp[numP][numB])