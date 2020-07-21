# 300. 最长上升子序列
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。


# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         if nums is None or len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         subStr = [[nums[0]]]
#         for k in range(1, len(nums)):
#             num = nums[k]
#             isInsert = False
#             for i in range(len(subStr) - 1, -1, -1):
#                 if num > subStr[i][-1]:
#                     if i == len(subStr) - 1 or len(subStr[i]) + 1 >= len(subStr[-1]):
#                         subStr.append([*subStr[i], num])
#                     else:
#                         lenSubStrT = len(subStr[i]) + 1
#                         for j in range(i+1, len(subStr)):
#                             if lenSubStrT < len(subStr[j]):
#                                 subStr.insert(j-1, [*subStr[i], num])
#                                 break
#                     isInsert = True
#                     break
#             if not isInsert:
#                 subStr.insert(0, [num])
#         return len(subStr[-1])


# dp
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if nums is None or len(nums) == 0: return 0
        if len(nums) == 1: return 1
        dp = [None] * len(nums)
        dp[0], maxLen = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] > dp[maxLen]:
                maxLen += 1
                dp[maxLen] = nums[i]
            elif nums[i] < dp[0]: dp[0] = nums[i]
            elif nums[i] > dp[0] and nums[i] < dp[maxLen]:
                l, r = 1, maxLen
                while r >= l:
                    if l == r:
                        dp[l] = nums[i]
                        break
                    mid = (l + r) >> 1
                    if nums[i] > dp[mid]:
                        if nums[i] < dp[mid + 1]:
                            dp[mid + 1] = nums[i]
                            break
                        elif nums[i] > dp[mid + 1]: l = mid + 1
                        elif nums[i] == dp[mid + 1]: break
                    elif nums[i] < dp[mid]:
                        if nums[i] > dp[mid - 1]:
                            dp[mid] = nums[i]
                            break
                        elif nums[i] < dp[mid - 1]: r = mid - 1
                        elif nums[i] == dp[mid - 1]: break
                    elif nums[i] == dp[mid]: break
        return maxLen + 1




s = Solution()
result = 4
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(nums))

result = 3
nums = [4,10,4,3,8,9]
print(s.lengthOfLIS(nums))

result = 6
nums = [3,5,6,2,5,4,19,5,6,7,12]
print(s.lengthOfLIS(nums))