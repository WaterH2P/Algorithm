# 1351. 统计有序矩阵中的负数
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
# 请你统计并返回 grid 中 负数 的数目。


class Solution:
    def countNegatives(self, grid) -> int:
        if grid is None or len(grid) == 0:
            return 0
        numOfNegatives = 0
        maxCol = len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, maxCol):
                if grid[i][j] < 0:
                    maxCol = j
                    break
            numOfNegatives += len(grid[0]) - maxCol
        return numOfNegatives



if __name__ == '__main__':
    s = Solution()
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]  # 8
    print(s.countNegatives(grid))
    grid = [[3, 2], [1, 0]]     # 0
    print(s.countNegatives(grid))
    grid = [[1, -1], [-1, -1]]  # 3
    print(s.countNegatives(grid))
