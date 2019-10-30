n = int(input().strip())
for k in range(n) :
    count = 0
    arr = sorted(list(map(int, input().strip().split())))
    sumNum = int(input().strip())
    l, r = 0, len(arr)-1
    while r > l :
        if arr[l] + arr[r] < sumNum :
            l += 1
        elif arr[l] + arr[r] > sumNum :
            r -= 1
        elif arr[l] + arr[r] == sumNum :
            count, l, r = map(lambda x: x+1, [count, l, r])
    print(count)