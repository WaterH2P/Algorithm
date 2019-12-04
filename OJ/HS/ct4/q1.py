# 最大和子数组
#
# Description:
# Given an array, the task is to complete the function which finds the maximum sum subarray,
# where you may remove at most one element to get the maximum sum.
#
# Input:
# 1
# 5
# 1, 2, 3, -4, 5
#
# Output:
# 11

for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    # Maximum sum subarrays in forward and backward
    # directions
    fw = [0 for k in range(n)]
    bw = [0 for k in range(n)]

    # Initialize current max and max so far.
    cur_max = max_so_far = arr[0]

    # calculating maximum sum subarrays in forward
    # direction
    for i in range(1, n):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum till ith, in
        # forward array
        fw[i] = cur_max

        # calculating maximum sum subarrays in backward
    # direction
    cur_max = max_so_far = bw[n - 1] = arr[n - 1]
    i = n - 2
    while i >= 0:
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum from ith, in
        # backward array
        bw[i] = cur_max
        i -= 1

    #  Initializing final ans by max_so_far so that,
    #  case when no element is removed to get max sum
    #  subarray is also handled
    fans = max_so_far

    #  choosing maximum ignoring ith element
    for i in range(1, n - 1):
        fans = max(fans, fw[i - 1] + bw[i + 1])

    fans = max(fans, fw[n-1], bw[0])

    print(fw)
    print(bw)
    print(fans)


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    fw = [0 for k in range(n)]
    bw = [0 for k in range(n)]
    cur_max = max_so_far = fw[0] = arr[0]
    for i in range(1, n):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)
        fw[i] = cur_max
    cur_max = max_so_far = bw[n - 1] = arr[n - 1]
    i = n - 2
    while i >= 0:
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)
        bw[i] = cur_max
        i -= 1
    fans = max_so_far
    for i in range(1, n - 1):
        fans = max(fans, fw[i - 1] + bw[i + 1])
    fans = max(fans, fw[n-1], bw[0])
    print(fw)
    print(bw)
    print(fans)

