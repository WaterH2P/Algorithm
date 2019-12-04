for t in range(int(input())):
    arr = list(map(int, input().split()))
    itvs = list(map(int, input().split()))
    n = len(arr)
    for itv in itvs:
        for i in range(n-itv):
            arr[i::itv] = sorted(arr[i::itv])
    print(*arr)