# 最小化初始点
for t in range(int(input())):
    r, c = map(int, input().split())
    arr = [int(_) for _ in input().split()]
    matrix = [[arr[i*c+j] for j in range(c)] for i in range(r)]
    dp = [[0 for j in range(c)] for i in range(r)]
    
    if matrix[-1][-1] > 0:
        dp[-1][-1] = 1
    else:
        dp[-1][-1] = abs(matrix[-1][-1]) + 1
    for i in range(r-2, -1, -1): dp[i][c-1] = max(dp[i+1][c-1]-matrix[i][c-1], 1)
    for j in range(c-2, -1, -1): dp[r-1][j] = max(dp[r-1][j+1]-matrix[r-1][j], 1)
    for i in range(r-2, -1, -1):
        for j in range(c-2, -1, -1):
            min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(min_points_on_exit-matrix[i][j], 1)
    print(*dp, sep='\n')
    print(dp[0][0])