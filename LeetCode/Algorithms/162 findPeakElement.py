# 162. 寻找峰值
# 峰值元素是指其值大于左右相邻值的元素。
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞。


# 递归
# class Solution:
#     def findPeakElement(self, nums) -> int:
#         if len(nums) == 1: return 0
#         if nums[0] > nums[1]: return 0
#         if nums[-1] > nums[-2]: return len(nums) - 1
#         def findPeak(nums, l, r):
#             if r - l == 1: return 0
#             if r - l == 2: return l if nums[l] > nums[l+1] else l+1
#             mid = (l + r) >> 1
#             if nums[mid - 1] < nums[mid] > nums[mid+1]: return mid
#             if nums[mid - 1] < nums[mid]: return findPeak(nums, mid, r)
#             else: return findPeak(nums, l, mid)
#         return findPeak(nums, 0, len(nums))

# 循环
class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums) - 1
        l, r = 0, len(nums)
        while l < r:
            if r - l == 1: return l
            if r - l == 2: return l if nums[l] > nums[l+1] else l+1
            mid = (l + r) >> 1
            if nums[mid - 1] < nums[mid] > nums[mid+1]: return mid
            if nums[mid - 1] < nums[mid]: l = mid
            else: r = mid


if __name__ == '__main__':
    s = Solution()

    nums = [1,2,3,1]
    print(s.findPeakElement(nums))

    nums = [1,2,1,3,5,6,4]
    print(s.findPeakElement(nums))

    nums = [3,2,1]
    print(s.findPeakElement(nums))

    nums = [1,2,3,2,1]
    print(s.findPeakElement(nums))

    nums = [1,2,1,2,1]
    print(s.findPeakElement(nums))