# 【中等】698. 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False
        nums.sort()
        if nums[-1] > target: return False

        


if __name__ == '__main__':
    s = Solution()

    result = True
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(s.canPartitionKSubsets(nums, k))
    print()

    result = False
    nums = [2,2,2,2,3,4,5]
    k = 4
    print(s.canPartitionKSubsets(nums, k))
    print()

    result = True
    nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    k = 3
    print(s.canPartitionKSubsets(nums, k))