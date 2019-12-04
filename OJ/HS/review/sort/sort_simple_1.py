for t in range(int(input())):
    n, *arr = list(map(int, input().split()))
    if n == 1:
        print(*arr)
        continue
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    print(*arr)
