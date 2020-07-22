# -*- coding: UTF-8 -*-
# 26. 删除排序数组中的重复项
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
  def removeDuplicates(self, nums):
    if len(nums) <= 1:
      return len(nums)
    else:
      l, r = 0, 1
      while r < len(nums):
        if (nums[l] < nums[r]):
          l = l + 1
          nums[l] = nums[r]
        r = r + 1
      return l + 1

if __name__ == '__main__':
  s = Solution()
  nums = [1,1,2]
  print(s.removeDuplicates(nums))
  print(nums)