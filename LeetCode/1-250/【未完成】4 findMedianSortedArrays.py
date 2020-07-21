# 【困难】4. 寻找两个有序数组的中位数
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i1, i2 = len(nums1)/2, len(nums2)/2

        return None


if __name__ == '__main__':
    s = Solution()
    result = s.findMedianSortedArrays()
    print(result)