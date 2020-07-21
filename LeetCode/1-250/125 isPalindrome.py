# 125. 验证回文串
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 本题中，我们将空字符串定义为有效的回文串。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isNumOrLetter(s):
            asciiS = ord(s)
            if 48 <= asciiS <= 57 or 65 <= asciiS <= 90 or 97 <= asciiS <= 122:
                return True
            else:
                return False

        s = ''.join(filter(str.isalnum, s)).lower()
        s = ''.join(filter(isNumOrLetter, s)).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()

    result = True
    strT = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(strT))
    print()

    result = False
    strT = "race a car"
    print(s.isPalindrome(strT))
    print()

    result = True
    strT = ".,"
    print(s.isPalindrome(strT))
    print()

    result = False
    strT = "0P"
    print(s.isPalindrome(strT))
