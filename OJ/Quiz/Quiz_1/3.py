

def quickSort(arr, left, right):
    count = 0

    partitionIndex = 0
    if not isinstance(left, int) or left < 0 :
        left = 0
    if not isinstance(right, int) or right >= len(arr) :
        right = len(arr) - 1

    if left < right :
        arr, partitionIndex, countT = partition(arr, left, right)
        count += countT
        arr, countT = quickSort(arr, left, partitionIndex-1)
        count += countT
        arr, countT = quickSort(arr, partitionIndex+1, right)
        count += countT

    return arr, count

def partition(arr, left, right):
    count = 0
    pivot = left
    index = pivot + 1
    i = index
    while i <= right :
        if arr[i] < arr[pivot] :
            if i > index :
                arr = swap(arr, i, index)
                count += 1
            index += 1
        i += 1     

    if pivot < index - 1 :
        arr = swap(arr, pivot, index - 1)
        count += 1
    return arr, index - 1, count

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int( input().strip() )
while n > 0 :
    length = int( input().strip() )
    nums = list( map(int, input().strip().split()) )
    if len(nums) > length :
        nums = nums[:length]
    nums, count = quickSort(nums, 0, len(nums)-1)
    print(count)
    n -= 1