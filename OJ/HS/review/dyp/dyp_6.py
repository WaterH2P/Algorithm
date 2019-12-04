# 无重复字符子集问题
def cor_bin(n):
    ans = 0
    for c in str(n):
        ans |= 1 << ord(c)-ord('0')
    return ans

def solve(arr, dp, n, flags):
    if n < 0: return 0
    if dp[n][flags]: return dp[n][flags]
    dp[n][flags] = solve(arr,dp,n-1,flags)
    a = cor_bin(arr[n])
    if flags ^ a == flags - a:
        dp[n][flags] = max(dp[n][flags], arr[n] + solve(arr,dp,n-1,flags^a))
    return dp[n][flags]

for t in range(int(input())):
    n, arr = int(input()), [int(_) for _ in input().split()]
    dp = [ [None] * 2**10 for _ in range(n) ]
    print(solve(arr, dp, n-1, 2**10-1))