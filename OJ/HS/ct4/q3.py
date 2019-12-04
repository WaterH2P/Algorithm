# 按照要求保留数组元素使得和最大
#
# Description:
# Given an array of N numbers, we need to maximize the sum of selected numbers. At each step,
# you need to select a number Ai, delete one occurrence of Ai-1 (if exists) and Ai each from the array. Repeat these
# steps until the array gets empty. The problem is to maximize the sum of selected numbers.
#
# Input:
# 2
# 3
# 1 2 3
# 6
# 1 2 2 2 3 4
#
# Output:
# 4
# 10


for t in range(int(input())):
    n = int(input())
    arr = sorted([int(a) for a in input().split()])
    sel = []
    while len(arr):
        n = len(arr)
        sel.append(arr[n - 1])
        if arr[n - 1] - 1 in arr:
            del arr[arr.index(arr[n - 1] - 1)]
            del arr[n - 2]
        else:
            del arr[n - 1]
    print(sum(sel))
