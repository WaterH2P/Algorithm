# 【简单】1496. 面试题 17.16. 按摩师

class Solution:
    def massage(self, nums) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return nums[0] if nums[0] > nums[1] else nums[1]
        if len(nums) == 3:
            return nums[0] + nums[2] if nums[0] + nums[2] > nums[1] else nums[1]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            for j in range(i-2, i-4, -1):
                if dp[j] + nums[i] > dp[i]:
                    dp[i] = dp[j] + nums[i]

        return dp[-1] if dp[-1] > dp[-2] else dp[-2]


if __name__ == '__main__':
    s = Solution()
    
    result = 4
    nums = [1,2,3,1]
    print(s.massage(nums))

    result = 12
    nums = [2,7,9,3,1]
    print(s.massage(nums))

    result = 2
    nums = [1,1,1]
    print(s.massage(nums))