# 买菜
#
# Description:
# Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable
# sellers in a line. Each vegetable seller sells all three vegetable items, but at different prices. Rahul,
# obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops. Also,
# Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop. Rahul wishes to spend minimum
# money buying vegetables using this strategy. Help Rahul determine the minimum money he will spend.
#
# Input:
# 1
# 3
# 1 50 50
# 50 50 50
# 1 50 50
#
# Output:
# 52


for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp)
    dp = [[0 for i in range(3)] for j in range(n)]
    dp[0][:] = a[0][:]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + a[i][j]
    ans = 10 ** 9
    for i in range(3):
        ans = min(ans, dp[n - 1][i])
    print(ans)
