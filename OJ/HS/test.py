c = int(input())
while c > 0:
    arr = list(map(int, input().split()))
    num = int(input())
    n = len(arr)
    c -= 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) > num:
                count += n-j
                break
    print(count)


