# 某部队举办了一届军事运动会，其中有一个团体马拉松项目，有n名选手按顺序从起跑线出发，并且记录下他们到达终点的顺序。
# 在跑步过程中超越了其他人的选手要给予表彰。
# 受表彰的选手需要满足的条件是，如果存在一名出发顺序排在选手X之后的选手Y先于X到达终点，则认为Y超越了X。
# 对于每一个选手，只要他超越了任意一个人，就有资格受到表彰。请你计算出有多少人可以得到表彰。

# 输入第一行仅包含一个正整数n，表示选手数量。(1<=n<=10^5)
# 输入第二行包含n个正整数，是一个1-n的排列A，表示出发顺序，A[i]表示第i个出发的选手的编号。
# 输入第三行同样包含一个1-n的排列B，表示到达顺序，B[i]表示第i个到达的选手的编号

# 输出仅包含一个整数，表示得到表彰的人数。

import sys

n = int(input().strip())
start = list(map(int, input().strip().split()))
end = list(map(int, input().strip().split()))

if n == 1: sys.stdout.write('0\n')
else:
    mem = [0 for _ in range(n)]
    for i in range(n):
        mem[start[i] - 1] = i

    i, curI = 0, mem[end[0]]
    j, minI = 0, float('inf')
    count = 0
    while i < n:
        if i == j:
            minI = float('inf')
            for k in range(i+1, n):
                if mem[end[k] - 1] < minI:
                    minI = mem[end[k] - 1]
                    j = k
        if mem[end[i] - 1] > minI:
            count += 1
        i += 1
    sys.stdout.write(str(count) + '\n')