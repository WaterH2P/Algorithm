u = int(input())
while u > 0:
    u -= 1
    arr = list(map(int, input().split()))

    def lis(a):  # a是待处理的数组
        n = len(a)
        f = [1] * n  # 初始化f
        for i in range(0, n):
            for j in range(0, i):
                if a[j] < a[i]:
                    f[i] = max(f[i], f[j] + 1)  # 最重要的一步
        return f  # 返回的是处理后的序列

    def lds(a):
        n = len(a)
        f = [1] * n
        for i in range(0, n):
            for j in range(0, i):
                if a[j] > a[i]:
                    f[i] = max(f[i], f[j] + 1)
        return f

    def path(f, a):
        r = []  # path 用于存储路径
        K = max(f)  # f 中的最大值
        N = f.index(max(f))  # 找到f最大值 的下标
        flag = N  # 从最大下标开始，遍历f，小于最大下标的，都可以直接跳过
        for i in f[N::-1]:  # 从后向前遍历,index 仍然是0,1,2,3；所以用了一个flag
            # print(i)
            if i == K:
                r.append(a[flag])  # 原数组
                K = K - 1
            flag = flag - 1
        # print('最长子序列', r[::-1])
        return r[::-1]

    tmp = list()
    for sep in range(1, len(arr)):
        arr1 = arr[:sep]
        arr2 = arr[sep:]
        arr2.reverse()
        left = path(lis(arr1), arr1)
        right = path(lis(arr2), arr2)
        right.reverse()
        print(left, right)
        left.extend(right)
        tmp.append(left)
    lens = list()
    for line in tmp:
        lens.append(len(line))
    max_len = max(lens)
    res = list()
    for index, line in enumerate(tmp):
        if lens[index] == max_len:
            res.append(line)
    new_list = [list(t) for t in set(tuple(_) for _ in res)]
    new_list.sort()
    for line in new_list:
        print(*line)
    print()
