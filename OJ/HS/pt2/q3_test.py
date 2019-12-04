for t in range(int(input())):
    n, *arr, k = input().split()
    n, k = int(n), int(k)
    for i in range(n//k):
        arr[i*k:i*k+k] = reversed(arr[i*k:i*k+k])
    print(*arr)
