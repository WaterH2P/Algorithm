for z in range(int(input().strip())):
    nums = list(map(int, input().strip().split(' ')))
    length = nums.pop(0)
    interval = nums.pop(-1)
    numsOutput = []
    i = 0
    while i + interval < len(nums):
        numsTemp = nums[i:i+interval]
        for num in numsTemp:
            numsOutput.insert(i, num)
        i = i + interval