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


# https://leetcode-cn.com/problems/two-sum/
if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([3, 2, 4], 6)
    print(result)