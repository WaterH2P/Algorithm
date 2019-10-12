n = int(input().strip())
for k in range(n) :
    count = 0
    length = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arrSort = sorted(arr)
    index = 0
    while index < len(arr) :
        if arr[index] == arrSort[index] :
            pass
        else :
            realIndex = arrSort.index(arr[index])
            arr[index], arr[realIndex] = arr[realIndex], arr[index]
            count += 1
            index -= 1
        index += 1
    print(count)