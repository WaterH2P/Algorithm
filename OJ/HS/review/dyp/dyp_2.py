# 数组查询
for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    fw = [0 for k in range(n)]
    bw = [0 for k in range(n)]
    cur_max = max_so_far = fw[0] = arr[0]
    for i in range(1, n):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)
        fw[i] = cur_max
    cur_max = max_so_far = bw[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)
        bw[i] = cur_max
    # 不删时的最大和
    res = max_so_far
    # 分别删除 1...n-1 时的最大和
    for i in range(1, n - 1):
        res = max(res, fw[i - 1] + bw[i + 1])
    # 删除 0, n 时的最大和
    res = max(res, fw[n-1], bw[0])
    print(res)