
def quickSort(arr, left, right):
    partitionIndex = 0
    if not isinstance(left, int) or left < 0 :
        left = 0
    if not isinstance(right, int) or right >= len(arr) :
        right = len(arr) - 1

    if left < right :
        arr, partitionIndex = partition(arr, left, right)
        arr = quickSort(arr, left, partitionIndex-1)
        arr = quickSort(arr, partitionIndex+1, right)

    return arr
 
def partition(arr, left ,right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right :
        if arr[i] < arr[pivot] :
            arr = swap(arr, i, index)
            index += 1
        i += 1     

    arr = swap(arr, pivot, index - 1)
    return arr, index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int( input().strip() )
while n > 0 :
    count = 0
    length = int( input().strip() )
    nums = list( map(int, input().strip().split()) )
    numSort = [x for x in nums]
    if len(nums) > length :
        nums = nums[:length]
        numSort = nums
    numSort = quickSort(numSort, 0, len(nums)-1)
    i = 0
    while i < len(nums) :
        j = i + 1
        while j < len(nums) and nums[i] != numSort[j]:
            j += 1
        if j < len(nums) and j > i :
            nums[i], nums[j] = nums[j], nums[i]
            i-= 1
            count += 1
        i+= 1
    n -= 1
    print(count)