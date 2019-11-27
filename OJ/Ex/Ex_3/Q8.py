for _ in range(int(input().strip())):
    length = int(input().strip())
    nums = list(map(int, input().strip().split()))
    numsCountDict = {}
    for num in nums:
        if num in numsCountDict:
            numsCountDict[num] += 1
        else:
            numsCountDict[num] = 1
    numsCountArray = []
    for num in numsCountDict:
        numsCountArray.append([num, numsCountDict[num]])
    numsCountArray.sort(reverse=True,key=lambda x:(x[1], -x[0]))
    printStr = ''
    for numCount in numsCountArray:
        for i in range(numCount[1]):
            printStr += str(numCount[0]) + ' '
    print(printStr.strip())