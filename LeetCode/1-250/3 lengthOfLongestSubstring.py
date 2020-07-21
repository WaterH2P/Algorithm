# 【中等】3. lengthOfLongestSubstring
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxS, tempS = [], []
        while l < len(s):
            if s[l] not in tempS:
                tempS.append(s[l])
                l += 1
            else:
                if len(tempS) > len(maxS):
                    maxS = [_ for _ in tempS]
                    index = tempS.index(s[l])
                    l = index + 1
                    r = l + 1
                else:
                    l = r
                    r += 1
                tempS = []
        if len(tempS) > len(maxS):
            maxS = [_ for _ in tempS]
        return len(maxS)


if __name__ == '__main__':
    s = Solution()
    result = s.lengthOfLongestSubstring('bbtablud')
    print(result)