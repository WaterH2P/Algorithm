for t in range(int(input())):
    k, n = map(int, input().split())
    boards = list(map(int, input().split()))
    # initialize table
    dp = [[0 for i in range(n + 1)]
          for j in range(k + 1)]

    # base cases
    # k=1
    for i in range(1, n + 1):
        dp[1][i] = sum(boards[0:i])

        # n=1
    for i in range(1, k + 1):
        dp[i][1] = boards[0]

        # 2 to k partitions
    for i in range(2, k + 1):  # 2 to n boards
        for j in range(2, n + 1):

            # track minimum
            best = 100000000

            # i-1 th separator before position arr[p=1..j]
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p],
                                     sum(boards[p:j])))

            dp[i][j] = best

            # required
    print(dp[k][n])

