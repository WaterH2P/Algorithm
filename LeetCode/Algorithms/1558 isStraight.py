# 面试题61. 扑克牌中的顺子
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        numOfZero = nums.count(0)
        for i in range(numOfZero + 1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False
        return nums[-1] - nums[numOfZero] <= 4


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]  # True
    print(s.isStraight(nums))
    nums = [0, 0, 1, 2, 5]  # True
    print(s.isStraight(nums))
    nums = [8, 8, 10, 12, 11]  # False
    print(s.isStraight(nums))
    nums = [11, 0, 9, 0, 0]  # True
    print(s.isStraight(nums))
    nums = [12, 13, 7, 10, 8]  # False
    print(s.isStraight(nums))
    nums = [1, 6, 5, 4, 2]  # False
    print(s.isStraight(nums))
