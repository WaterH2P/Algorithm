# 1394 面试题 01.06. 字符串压缩
# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
# 比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。


class Solution:
    def compressString(self, S: str) -> str:
        if len(S) <= 1: return S
        res, pre = '', 0
        for i in range(1, len(S)):
            if S[i] != S[pre]:
                res += S[pre] + str(i - pre)
                pre = i
        res += S[pre] + str(len(S) - pre)
        return res if len(res) < len(S) else S

if __name__ == '__main__':
    s = Solution()

    result = "a2b1c5a3"
    S = "aabcccccaaa"
    print(s.compressString(S))

    result = "abbccd"
    S = "abbccd"
    print(s.compressString(S))