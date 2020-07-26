# -*- coding: UTF-8 -*-
# 120. 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

class Solution:
  def minimumTotal(self, triangle) -> int:
    if not triangle or len(triangle) == 0: return 0
    self.row = len(triangle)
    self.mem = [[0] * len(_) for _ in triangle]
    
    def dfs(x, y):
      if self.mem[x][y] == 0:
        if x < self.row - 1:
          self.mem[x][y] = min(dfs(x + 1, y), dfs(x + 1, y + 1)) + triangle[x][y]
        else:
          self.mem[x][y] = triangle[x][y]
      return self.mem[x][y]
    
    return dfs(0, 0)

if __name__ == "__main__":
  s = Solution()
  triangle = [
      [2],
      [3,4],
    [6,5,7],
    [4,1,8,3]
  ]
  print(s.minimumTotal(triangle))

