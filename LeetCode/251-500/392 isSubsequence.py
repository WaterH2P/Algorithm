# -*- coding: UTF-8 -*-
# 392. 判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    index, isNotFind = 0, False
    for st in s:
      isNotFind = True
      for i in range(index, len(t)):
        if t[i] == st:
          isNotFind = False
          index = i + 1
          break
      if isNotFind: return False
    return True

if __name__ == "__main__":
  s = Solution()
  a = "aaaaaa"
  b = "bbaaaa"
  print(s.isSubsequence(a, b))