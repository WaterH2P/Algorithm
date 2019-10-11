import itertools

def minAbs(arr):
    sumAll = sum(arr)
    minDis = -1
    for arrT in itertools.combinations(arr, int(len(arr)/2)) :
        if minDis < 0 or abs(sum(arrT)-(sumAll - sum(arrT))) < minDis:
            minDis = abs(sum(arrT)-(sumAll - sum(arrT)))
    return minDis

n = int(input().strip())
for k in range(n) :
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    arr = [*arr1, *arr2]
    print(minAbs(arr))