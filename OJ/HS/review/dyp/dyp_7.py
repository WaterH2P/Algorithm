# 矩阵计算
for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = ((i*j)**3) % 7
            if tmp != 0 and tmp != 1 and tmp != 5:
                cnt += 1
    print(cnt)