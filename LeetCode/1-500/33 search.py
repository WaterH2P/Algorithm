# 【中等】33. 搜索旋转排序数组
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。


class Solution:
    def search(self, nums, target: int) -> int:
        if not len(nums): return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1

        def logSearch(nums, l, r, target):
            if target == nums[l] : return l
            if target == nums[r] : return r
            if r - 1 <= l <= r:
                return -1
            
            mid = (l + r) // 2
            if target == nums[mid] : return mid
            if nums[l] < target:
                if target < nums[mid]: return logSearch(nums, l, mid, target)
                else:
                    if nums[l] < nums[mid]: return logSearch(nums, mid, r, target)
                    else: return logSearch(nums, l, mid, target)
            else:
                if nums[mid] < target: return logSearch(nums, mid, r, target)
                else:
                    if nums[l] < nums[mid]: return logSearch(nums, mid, r, target)
                    else: return logSearch(nums, l, mid, target)
        
        return logSearch(nums, 0, len(nums) - 1, target)

if __name__ == '__main__':
    s = Solution()

    result = 4
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))

    result = -1
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(s.search(nums, target))
                
