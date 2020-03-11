# 46. 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列。

class Solution:
    def permute(self, nums):
        def f(nums, rank, res):
            if len(nums) == 1:
                res.append([*rank, nums[0]])
                return res
            for i in range(len(nums)):
                rank.append(nums[i])
                if i < len(nums) - 1:
                    f([*nums[0:i], *nums[i+1:]], rank, res)
                else:
                    f(nums[0:i], rank, res)
                rank.pop(-1)
            return res
        return f(nums, [], [])

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))