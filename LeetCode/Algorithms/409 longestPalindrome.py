# 【简单】409. 最长回文串
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。


import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = collections.Counter(s)
        return len(s) - max(0, sum(ss[letter] & 1 for letter in ss) - 1)


if __name__ == '__main__':
    s = Solution()

    result = 7
    strT = "abccccdd"
    print(s.longestPalindrome(strT))
        