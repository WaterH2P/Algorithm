class Solution:
    def tictactoe(self, moves) -> str:
        grid = [([None] * 3) for _ in range(3)]
        steps = min(len(moves), 9)
        if steps % 2 == 0:
            for i in range(1, steps, 2):
                grid[moves[i][0]][moves[i][1]] = 'B'
        else:
            for i in range(0, steps, 2):
                grid[moves[i][0]][moves[i][1]] = 'A'
        
        if steps < 4:
            return 'Pending'
        x, y = moves[-1]
        if grid[x][0] != None and grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0]
        if grid[0][y] != None and grid[0][y] == grid[1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]
        if x == y and grid[0][0] != None and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            return grid[0][0]
        if x + y == 2 and grid[0][2] != None and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            return grid[0][2]
        return 'Draw' if steps >= 9 else 'Pending'

moves = [[0,2],[2,0],[2,1],[0,1],[1,2]]
s = Solution()
print( s.tictactoe(moves) )