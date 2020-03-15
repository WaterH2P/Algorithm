# 695. 岛屿的最大面积


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxArea = 0
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i, j, grid, visit, area):
            area += 1
            visit[i][j] = True
            if i > 0 and grid[i-1][j] and not visit[i-1][j]:
                area = dfs(i-1, j, grid, visit, area)
            if i < len(grid) - 1 and grid[i+1][j] and not visit[i+1][j]:
                area = dfs(i+1, j, grid, visit, area)
            if j > 0 and grid[i][j-1] and not visit[i][j-1]:
                area = dfs(i, j-1, grid, visit, area)
            if j < len(grid[0]) - 1 and grid[i][j+1] and not visit[i][j+1]:
                area = dfs(i, j+1, grid, visit, area)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visit[i][j]:
                    area = dfs(i, j, grid, visit, 0)
                    if area > maxArea: maxArea = area
        return maxArea

if __name__ == '__main__':
    s = Solution()
    result = 6
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))

    result = 0
    grid = [[0,0,0,0,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))
