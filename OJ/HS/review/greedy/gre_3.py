# 时间与收益
for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    arr = [[arr[i * 3 + j] for j in range(3)] for i in range(n)]
    arr.sort(key=lambda a: -a[2])
    result = [False] * n
    profit = 0
    count = 0
    for i in range(n):
        for j in range(min(n - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                profit += arr[i][2]
                count += 1
                break
    print(count, profit)