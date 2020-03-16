# 921. 使括号有效的最少添加
# 给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。
# 从形式上讲，只有满足下面几点之一，括号字符串才是有效的：
# 它是一个空字符串，或者
# 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
# 它可以被写作 (A)，其中 A 是有效字符串。
# 给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l, r = 0, 0
        for s in S:
            if s == '(': l += 1
            elif s == ')':
                if l > 0: l -= 1
                else: r += 1
        return l + r

if __name__ == '__main__':
    s = Solution()

    result = 1
    S = "())"
    print(s.minAddToMakeValid(S))

    result = 3
    S = "((("
    print(s.minAddToMakeValid(S))
    
    result = 0
    S = "()"
    print(s.minAddToMakeValid(S))

    result = 4
    S = "()))(("
    print(s.minAddToMakeValid(S))