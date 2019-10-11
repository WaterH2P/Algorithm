n = int(input().strip())
for k in range(n) :
    arr = list(map(int, input().strip().split()))
    l, r = map(int, input().strip().split())
    K = int(input().strip())
    arr = arr[l-1:r]
    arr.sort()
    print(arr[K-1])