# -*- coding: UTF-8 -*-
# 329. 矩阵中的最长递增路径
# 给定一个整数矩阵，找出最长递增路径的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

class Solution:
  def longestIncreasingPath(self, matrix) -> int:
    if not matrix or len(matrix) == 0: return 0
    self.row, self.col = len(matrix), len(matrix[0])
    self.mem = [[0] * self.col for _ in range(self.row)]

    def dfs(x, y):
      if self.mem[x][y] == 0:
        if x > 0 and matrix[x][y] < matrix[x - 1][y]: self.mem[x][y] = max(self.mem[x][y], 1 + dfs(x - 1, y))
        if y > 0 and matrix[x][y] < matrix[x][y - 1]: self.mem[x][y] = max(self.mem[x][y], 1 + dfs(x, y - 1))
        if x < self.row - 1 and matrix[x][y] < matrix[x + 1][y]: self.mem[x][y] = max(self.mem[x][y], 1 + dfs(x + 1, y))
        if y < self.col - 1 and matrix[x][y] < matrix[x][y + 1]: self.mem[x][y] = max(self.mem[x][y], 1 + dfs(x, y + 1))
      return self.mem[x][y]

    maxLen = 0
    for i in range(self.row):
      for j in range(self.col):
        if self.mem[i][j] == 0:
          maxLen = max(maxLen, dfs(i, j))
    return maxLen + 1

if __name__ == "__main__":
  s = Solution()
  matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
  ]
  print(s.longestIncreasingPath(matrix))