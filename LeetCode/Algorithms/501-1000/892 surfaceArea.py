# 【简单】892. 三维形体的表面积
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 请你返回最终形体的表面积。


class Solution:
    def surfaceArea(self, grid) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += grid[i][j] * 4 + 2
                    if i > 0: res -= min(grid[i][j], grid[i-1][j])
                    if i < len(grid) - 1: res -= min(grid[i][j], grid[i+1][j])

                    if j > 0: res -= min(grid[i][j], grid[i][j-1])
                    if j < len(grid[0]) - 1: res -= min(grid[i][j], grid[i][j+1])
        return res


if __name__ == '__main__':
    s = Solution()

    result = 10
    grid = [[2]]
    print(s.surfaceArea(grid))

    result = 34
    grid = [[1,2],[3,4]]
    print(s.surfaceArea(grid))

    result = 16
    grid = [[1,0],[0,2]]
    print(s.surfaceArea(grid))