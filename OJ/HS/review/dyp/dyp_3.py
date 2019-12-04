# 按照要求保留数组元素使得和最大
for t in range(int(input())):
    n = int(input())
    arr = sorted([int(a) for a in input().split()])
    sel = []
    while len(arr):
        n = len(arr)
        sel.append(arr[-1])
        if arr[-1] - 1 in arr:
            del arr[arr.index(arr[-1] - 1)]
            del arr[-1]
        else:
            del arr[-1]
    print(sum(sel))