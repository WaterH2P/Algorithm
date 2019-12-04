# Given the list of coins of distinct denominations and total amount of money. 
# Output the minimum number of coins required to make up that amount. 
# Output -1 if that money cannot be made up using given coins. 
# You may assume that there are infinite numbers of coins of each type.

def f1(coins, total, dp):
    if dp[total - 1] != -2:
        return dp[total -1]
    count = 999
    for coin in coins:
        if coin == total:
            count = 1
            break
        elif coin < total:
            countT = f1(coins, total-coin, dp)
            if countT == -1:
                if count == 999:
                    count = -1
            else:
                if count == -1:
                    count = countT + 1
                else:
                    count = min(count, countT + 1)
    dp[total - 1] = count if count != 999 else -1
    return dp[total - 1]

for _ in range(int(input().strip())):
    n, total = map(int, input().strip().split())
    coins = list(map(int, input().strip().split()))
    dp = [-2]*total
    coins.sort(reverse=True)
    count = f1(coins, total, dp)
    print(count)