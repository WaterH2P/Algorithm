class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:return [] 

        dp = [0 for _ in range(len(nums)-k+1)]
        dp[0] = max(nums[:k])
        for i in range(1,len(nums)-k+1):
            if nums[i-1] != dp[i-1]:
                dp[i] = max(dp[i-1],nums[i+k-1])
            else:
                dp[i] = max(nums[i:i+k])
        return dp