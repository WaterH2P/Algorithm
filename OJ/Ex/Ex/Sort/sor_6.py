# Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.
# Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.

for _ in range(int(input().strip())) :
    count = 0
    length = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arrSort = sorted(arr)
    index = 0
    while index < len(arr) :
        if arr[index] != arrSort[index] :
            realIndex = arrSort.index(arr[index])
            arr[index], arr[realIndex] = arr[realIndex], arr[index]
            count += 1
            index -= 1
        index += 1
    print(count)