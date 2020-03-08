class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in coins:
            dp[i] = 1
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0 and dp[i-j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-j] + 1
                    elif dp[i] != 1:
                        dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]

coins = [2]
amount = 11
s = Solution()
print( s.coinChange(coins, amount) )