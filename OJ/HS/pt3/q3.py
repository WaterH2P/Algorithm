for t in range(int(input())):
    arr = list(map(int, input().split()))
    intervals = list(map(int, input().split()))
    for interval in intervals:
        for i in range(len(arr)-interval):
            arr[i::interval] = sorted(arr[i::interval])
    print(*arr)

