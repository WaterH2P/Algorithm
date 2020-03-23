# 【中等】646. 最长数对链
# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
# 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
# 给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。


# dp
# class Solution:
#     def findLongestChain(self, pairs) -> int:
#         pairs.sort()
#         dp = [1] * len(pairs)
#         for i in range(1, len(dp)):
#             for j in range(i-1, -1, -1):
#                 if dp[j] > 1:
#                     if pairs[i][0] > pairs[j][1]:
#                         dp[i] = dp[j] + 1
#                         break
#             if dp[i] == 1:
#                 for j in range(0, i):
#                     if pairs[i][0] > pairs[j][1]:
#                         dp[i] = 2
#                         break
#         return dp[-1]


class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort(key=lambda x: x[1])
        res, tmp = 1, pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > tmp:
                res += 1
                tmp = pairs[i][1]
        return res


if __name__ == "__main__":
    s = Solution()

    result = 2
    pairs = [[1,2], [2,3], [3,4]]
    print(s.findLongestChain(pairs))
    print()

    result = 4
    pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
    print(s.findLongestChain(pairs))
    print()

    result = 3
    pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
    print(s.findLongestChain(pairs))


