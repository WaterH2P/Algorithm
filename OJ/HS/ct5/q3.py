for u in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    arr = [[arr[i * 3 + j] for j in range(3)] for i in range(n)]
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    t = 3
    result = [False] * t
    job = ['-1'] * t
    profit = 0
    count = 0
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                profit += arr[i][2]
                count += 1
                break
    print(count, profit)
