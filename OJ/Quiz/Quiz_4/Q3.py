for z in range(int(input().strip())):
    length = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums.sort()
    maxSum = 0
    while len(nums) > 0:
        maxNum = nums.pop(-1)
        maxSum += maxNum
        if maxNum-1 in nums:
            nums.pop(nums.index(maxNum-1))
    print(maxSum)