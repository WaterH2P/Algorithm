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


# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
if __name__ == '__main__':
    s = Solution()
    result = s.lengthOfLongestSubstring('bbtablud')
    print(result)