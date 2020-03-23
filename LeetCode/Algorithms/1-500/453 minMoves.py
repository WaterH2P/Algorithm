# 【简单】453. 最小移动次数使数组元素相等
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。


class Solution:
    def minMoves(self, nums) -> int:
        if len(nums) <= 1: return 0
        nums.sort(reverse=True)

        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                res += i * (nums[i-1] - nums[i])
        return res


class Solution:
    def minMoves(self, nums) -> int:
        res = 0
        minNum = float('inf')
        for num in nums:
            if num < minNum: minNum = num
            res += num
        return res - minNum * len(nums)


if __name__ == '__main__':
    s = Solution()

    result = 3
    nums = [1,2,3]
    print(s.minMoves(nums))
