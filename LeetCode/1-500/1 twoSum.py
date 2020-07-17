# 【简单】1. 两数之和
# https://leetcode-cn.com/problems/two-sum/
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。



class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort(key=lambda x: x[0])
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l][0] + nums[r][0] < target:
                l += 1
            elif nums[l][0] + nums[r][0] == target:
                return [nums[l][1], nums[r][1]]
            elif nums[l][0] + nums[r][0] > target:
                r -= 1


if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([3, 2, 4], 6)
    print(result)