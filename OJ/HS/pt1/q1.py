for u in range(int(input())):
    arr, num = list(map(int, input().split())), int(input())
    n = len(arr)
    qmax, qmin = list(), list()
    i, j, count = [0] * 3
    while i < n:
        while j < n:
            while len(qmax) != 0 and arr[j] >= arr[qmax[-1]]:
                qmax.pop()
            qmax.append(j)
            while len(qmin) != 0 and arr[j] <= arr[qmin[-1]]:
                qmin.pop()
            qmin.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmax[0] == i:
            qmax.pop(0)
        if qmin[0] == i:
            qmin.pop(0)
        count += n - j
        i += 1
    print(count)

