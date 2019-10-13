import itertools
n = int(input().strip())
for k in range(n) :
    arr1, arr2 = list(map(int, input().strip().split())), list(map(int, input().strip().split()))
    arr, sumAll, minDis = [*arr1, *arr2], sum([*arr1, *arr2]), 999
    for arrT in itertools.combinations(arr, int(len(arr)/2)) :
        minDis = min(minDis, abs(sum(arrT)-(sumAll - sum(arrT))))
    print(minDis)