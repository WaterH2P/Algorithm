def countDZ(nums, s, e):
    if e - s <= 1:
        return 0
    numsT = nums[s:e]
    midNum = numsT.pop(0)
    numsTl = []
    numsTr = []
    for num in numsT:
        if num < midNum:
            numsTl.append(num)
        else:
            numsTr.append(num)
    numsT = [*numsTl, midNum, *numsTr]
    j = 0
    for i in range(s, e):
        nums[i] = numsT[j]
        j += 1
    countDZ(nums, s, e - len(numsTr) - 1)
    countDZ(nums, e - len(numsTr), e)
    return


for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    pos = {}
    
    for i in range(n):
        pos[nums[i]] = i
    countDZ(nums, 0, n)
    count = 0
    for i in range(n):
        num = nums[i]
        if pos[num] < i:
            count += i - pos[num]
    print(pos)
    print(count)