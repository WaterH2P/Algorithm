
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
    len1, len2 = map(int, input().strip().split())
    nums1 = list( map(int, input().strip().split()) )
    nums2 = list( map(int, input().strip().split()) )
    count = {}
    if len(nums1) > len1 :
        nums1 = nums1[:len1]
    if len(nums2) > len2 :
        nums2 = nums2[:len2]
    i = 0
    while i < len(nums1) :
        index = nums1[i]
        if index in count.keys():
            count[index] += 1
        else :
            count[index] = 1
        i+= 1
    output = ''
    i = 0
    while i < len(nums2) :
        j = count[ nums2[i] ]
        while j > 0 :
            output += str(nums2[i]) + ' '
            j -= 1
        count.pop(nums2[i])
        i += 1
    i = 0
    countKeys = [x for x in count.keys()]
    countKeys.sort()
    for i in countKeys :
        j = count[i]
        while j > 0 :
            output += str(i) + ' '
            j -= 1
        i += 1
    print(output.strip())
    n -= 1