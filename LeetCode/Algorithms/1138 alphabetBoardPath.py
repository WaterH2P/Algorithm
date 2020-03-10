# 1138. 字母板上的路径
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].
# 我们可以按下面的指令规则行动：
    # 如果方格存在，'U' 意味着将我们的位置上移一行；
    # 如果方格存在，'D' 意味着将我们的位置下移一行；
    # 如果方格存在，'L' 意味着将我们的位置左移一列；
    # 如果方格存在，'R' 意味着将我们的位置右移一列；
    # '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
# 返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res, pos = '', [0, 0]
        for s in target:
            dis = [(ord(s) - 97) // 5, (ord(s) - 97) % 5]
            while pos[0] != dis[0] or pos[1] != dis[1]:
                if dis[0] == 5:
                    if pos[1] > 0:
                        res += 'L' * (pos[1] - 0)
                        pos[1] = 0
                    if pos[0] < 5:
                        res += 'D' * (5 - pos[0])
                        pos[0] = 5
                elif pos[0] == 5:
                    if dis[0] < 5:
                        res += 'U' * (5 - dis[0])
                        pos[0] = dis[0]
                    if dis[1] > 0:
                        res += 'R' * (dis[1] - 0)
                        pos[1] = dis[1]
                else:
                    if pos[0] < dis[0]:
                        res += 'D' * (dis[0] - pos[0])
                        pos[0] = dis[0]
                    elif pos[0] > dis[0]:
                        res += 'U' * (pos[0] - dis[0])
                        pos[0] = dis[0]
                    if pos[1] < dis[1]:
                        res += 'R' * (dis[1] - pos[1])
                        pos[1] = dis[1]
                    elif pos[1] > dis[1]:
                        res += 'L' * (pos[1] - dis[1])
                        pos[1] = dis[1]
            res += '!'
        return res

if __name__ == '__main__':
    s = Solution()
    target = "leet"
    # target = "code"
    # target = 'zb'
    print( s.alphabetBoardPath(target) )