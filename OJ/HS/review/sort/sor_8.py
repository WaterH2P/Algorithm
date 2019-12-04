for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt += 1
    print(cnt)