# 【简单】1431. 面试题 08.03. 魔术索引
# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
# 给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

# 暴力法
class Solution:
    def findMagicIndex(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i: return i
            i = nums[i] if nums[i] > i else i + 1
        return -1


# 二分法
class Solution:
    def findMagicIndex(self, nums) -> int:
        def find(nums, l, r):
            if r < l: return -1
            if r == l: return l if nums[l] == l else -1
            if r == l + 1:
                if nums[l] == l: return l
                if nums[r] == r: return r
                return -1
            mid = (l + r) // 2
            if nums[mid] == mid: return mid
            index = find(nums, l, min(mid - 1, nums[mid]))
            return index if index > -1 else find(nums, max(mid + 1, nums[mid]), r)
        return find(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()

    result = 0
    nums = [0, 2, 3, 4, 5]
    print(s.findMagicIndex(nums))

    result = 1
    nums = [1, 1, 1]
    print(s.findMagicIndex(nums))

    result = 0
    nums = [0, 0, 2]
    print(s.findMagicIndex(nums))