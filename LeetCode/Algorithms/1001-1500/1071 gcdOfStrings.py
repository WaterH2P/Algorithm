# 1071. 字符串的最大公因子
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        maxGcd, remainder = len(str1), len(str2)
        while remainder != 0:
            maxGcd, remainder = remainder, maxGcd % remainder
        return str1[:maxGcd]

if __name__ == '__main__':
    s = Solution()

    result = 'ABC'
    str1 = 'ABCABC'
    str2 = 'ABC'
    print(s.gcdOfStrings(str1, str2))

    result = 'AB'
    str1 = 'ABABAB'
    str2 = 'ABAB'
    print(s.gcdOfStrings(str1, str2))

    result = ''
    str1 = 'LEET'
    str2 = 'CODE'
    print(s.gcdOfStrings(str1, str2))
        