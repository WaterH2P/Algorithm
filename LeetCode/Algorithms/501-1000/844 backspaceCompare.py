# 【简单】844. 比较含退格的字符串
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str1 = str2 = ''
        for s in S:
            if s == '#': str1 = str1[:-1]
            else: str1 += s
        for s in T:
            if s == '#': str2 = str2[:-1]
            else: str2 += s
        return str1 == str2


if __name__ == '__main__':
    s = Solution()

    result = True
    S = "ab#c"
    T = "ad#c"
    print(s.backspaceCompare(S, T))

    result = True
    S = "ab##"
    T = "c#d#"
    print(s.backspaceCompare(S, T))

    result = False
    S = "a#c"
    T = "b"
    print(s.backspaceCompare(S, T))