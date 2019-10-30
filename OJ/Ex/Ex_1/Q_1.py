def fn(arr, num):
    l, r, count = 0, 1, 0
    while l < len(arr) - 1 :
        minVal, maxVal = min(arr[l], arr[r]), max(arr[l], arr[r])
        if maxVal - minVal > num :
            count = count + len(arr) - r
            l += 1
            if r == l :
                r += 1
        else :
            r += 1
        if r == len(arr) :
            l += 1
            r = l + 1
    return count

n = int(input().strip())
for k in range(n) :
    arr = list(map(int, input().strip().split()))
    num = int(input().strip())
    print(fn(arr, num))