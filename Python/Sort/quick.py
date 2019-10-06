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

L = [2, 5, 7, 1, 4, 3, 0]
L2 = quickSort(L, 0, len(L)-1)
print(L2)


L = [1, 2, 3, 4, 5]
L2 = quickSort(L, 0, len(L)-1)
print(L2)