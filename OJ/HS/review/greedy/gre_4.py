# 硬币最小数量
for t in range(int(input())):
    n, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    coins.sort()
    cnt = 0
    while amount >= coins[0]:
        for i in range(len(coins)-1, -1, -1):
            if coins[i] <= amount:
                break
        amount -= coins[i]
        cnt += 1
    if amount:
        print(-1)
    else:
        print(cnt)
