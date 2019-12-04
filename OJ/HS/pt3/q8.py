import sys

t = int(input())
n = int(input())
lineNum = 1
for line in sys.stdin:
    lineNum += 1
    if lineNum % 2 == 1:
        continue
    nums = list(map(int, line.split()))
    resDict = dict()
    for num in nums:
        if num not in resDict:
            resDict[num] = 1
        else:
            resDict[num] += 1
    counted_nums = [(val, resDict[val]) for val in nums]
    counted_nums.sort(key=lambda a: (-a[1], a[0]))
    res = [val for (val, times) in counted_nums]
    print(*res)
