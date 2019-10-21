n = int(input().strip())
for t in range(n):
    numP, numB = map(int, input().split())
    boards = list(map(int, input().split()))
    dp = [[0 for i in range(numB)] for j in range(numP)]
    for i in range(0, numB) :
        dp[0][i] = sum(boards[0:i+1])
    for i in range(0, numP) :
        dp[i][0] = boards[0]
    for i in range(1, numP) :
        for j in range(1, numB) :
            maxT = 9999
            for k in range(0, j + 1) :
                maxT = min(maxT, max(dp[i - 1][k], sum(boards[k:j])))
                dp[i][j] = maxT
                print('')
                for dpt in dp : print(dpt)
                print('')
    print(dp[numP-1][numB-1])