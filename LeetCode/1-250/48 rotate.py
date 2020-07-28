# -*- coding: UTF-8 -*-
# 48. 旋转图像
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

class Solution:
  def rotate(self, matrix) -> None:
    if not matrix or len(matrix) == 0: return None
    m, n = len(matrix), len(matrix[0])
    for i in range(0, (m + 1) // 2):
      for j in range(i, n - 1 - i):
        matrix[i][j], matrix[j][n - 1 - i], matrix[m - 1 - i][n - 1 - j], matrix[m - 1 - j][i] = matrix[m - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[m - 1 - i][n - 1 - j]

if __name__ == "__main__":
  s = Solution()
  matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
  ]
  s.rotate(matrix)
  for i in range(len(matrix)):
    print(matrix[i])