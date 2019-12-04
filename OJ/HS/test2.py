c = int(input())
while c > 0:
    arr = list(map(int, input().split()))
    num = int(input())
    n = len(arr)
    c -= 1
    i = 0
    j = 1
    count = 0
    while i < n:
        while j < n:
            if max(arr[i:j+1]) - min(arr[i:j+1]) > num:
                count += n - j
                break
            j += 1
        i += 1
    print(count)




