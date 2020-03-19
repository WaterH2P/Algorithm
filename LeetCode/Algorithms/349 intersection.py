# 【简单】349. 两个数组的交集
# 给定两个数组，编写一个函数来计算它们的交集。


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    s = Solution()

    result = [2]
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(s.intersection(nums1, nums2))

    result = [9, 4]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1, nums2))