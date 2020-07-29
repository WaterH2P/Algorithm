# -*- coding: UTF-8 -8-
# LCP 13. 寻宝
# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
# 迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
# 要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。
# 迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。
# 我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

class Solution:
  def minimalSteps(self, maze) -> int:
    maze = [[*row] for row in maze]
    m, n = len(maze), len(maze[0])

    for i in range(m): print(maze[i])
    print('\n')

    # 利用 bfs 找到 start 到 end 最短路径长度，没有返回 -1
    def minRoad(start, end) -> int:
      visit = [[False] * n for _ in range(m)]
      # bfs 存储每一层遍历到达的位置，第一层为 start
      bfs = [[(start[0], start[1])]]
      visit[start[0]][start[1]] = True
      # arrive: 是否到达 end
      # forward: 本次 bfs 是否前进
      arrive, forward = False, True
      while not arrive and forward:
        forward = False
        bfs.append([])
        for posX, posY in bfs[-2]:
          neighbors = [[posX - 1, posY], [posX + 1, posY], [posX, posY - 1], [posX, posY + 1]]
          for [x, y] in neighbors:
            # 坐标合法、未被访问、不是墙壁
            if 0 <= x < m and 0 <= y < n and not visit[x][y] and maze[x][y] != '#':
              bfs[-1].append((x, y))
              forward = visit[x][y] = True
              if x == end[0] and y == end[1]:
                arrive = True
                break
          if arrive: break
      return len(bfs) - 1 if arrive else -1
    
    S, T, Ms, Os = (), (), [], []
    for i in range(m):
      for j in range(n):
        if maze[i][j] == 'M': Ms.append((i, j))
        elif maze[i][j] == 'O': Os.append((i, j))
        elif maze[i][j] == 'S': S = (i, j)
        elif maze[i][j] == 'T': T = (i, j)

    if len(Ms) == 0: return minRoad(S, T)
    else:
      cur, total = S, 0
     
      while len(Ms) > 0:
        minLen, minIndex = float('inf'), -1
        # 不在石堆，去石堆
        if maze[cur[0]][cur[1]] != 'O':
          for i in range(len(Os)):
            O = Os[i]
            minR = minRoad(cur, O)
            if 0 < minR < minLen: minLen, minIndex = minR, i
          if minLen == float('inf'): return -1
          else:
            print('去石堆1：', cur, ' -> ', Os[minIndex])
            cur = Os[minIndex]
            total += minLen
        # 在石堆，去机关
        else:
          for i in range(len(Ms)):
            M = Ms[i]
            minR = minRoad(cur, M)
            if 0 < minR < minLen: minLen, minIndex = minR, i
          if minLen == float('inf'): return -1
          else:
            print('去机关2：', cur, ' -> ', Ms[minIndex])
            cur = Ms[minIndex]
            Ms.pop(minIndex)
            total += minLen
      
      minLen = minRoad(cur, T)
      return total + minLen if minLen != -1 else -1

if __name__ == "__main__":
  s = Solution()
  # 16
  maze = ["S#O", "M..", "M.T"]
  # 17
  # maze = ["S#O", "M.T", "M.."]
  # -1
  # maze = ["S#O", "M.#", "M.T"]
  # 28
  # maze = [".MM..", "#..M.", ".#..#", "..O..", ".S.OM", ".#M#T", "###..", "....."]
  # -1
  # maze = ["S.#.M","O.#.O","M.#.T"]
  # 60
  # maze = ["......", "M....M", ".M#...", "....M.", "##.TM.", "...O..", ".S##O.", "M#..M.", "#....."]
  print(s.minimalSteps(maze))