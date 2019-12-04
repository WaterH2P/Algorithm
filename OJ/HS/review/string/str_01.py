# 对称子字符串
def find(arr, k):
    i = 0
    while i + 2 * k <= len(arr):
        if sum(arr[i:i+k]) == sum(arr[i+k:i+k+k]):
            return k + k
        i += 1
    return find(arr, k - 1)


for t in range(int(input())):
    arr = [int(c) for c in input()]
    k = len(arr) // 2
    print(find(arr, k))