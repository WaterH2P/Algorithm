def minAbs(arr1, arr2):
    arr1, arr2 = map(sorted, [arr1, arr2])
    minDis = sum(arr1) - sum(arr2)
    if minDis == 0 :
        return 0
    elif minDis > 0 :
        arr1, arr2 = arr2, arr1
    minDis = abs(minDis)

    isExchange = True
    while isExchange :
        isExchange = False
        index = len(arr2) - 1
        while index > 0 and minDis > 0:
            minVal, maxVal = arr1[0], arr2[index]
            if minVal >= maxVal :
                break
            if maxVal - minVal < minDis :
                isExchange = True
                minDis = abs(minDis - 2 * maxVal + 2 * minVal)
                arr1[0], arr2[index] = maxVal, minVal
                arr1, arr2 = map(sorted, [arr1, arr2])
                index = len(arr2) - 1
            index -= 1
    return minDis

n = int(input().strip())
for k in range(n) :
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    minDis = minAbs(arr1, arr2)
    print(minDis)