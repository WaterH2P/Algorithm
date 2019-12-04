import sys

t = int(input())
n = int(input())
lineNum = 1
for line in sys.stdin:
    lineNum += 1
    if lineNum % 2 == 1:
        continue
    nums = list(map(int, line.split()))
    count = 0
    for index, num1 in enumerate(nums):
        for num2 in nums[index+1:]:
            if num1 > num2:
                count += 1
    print(count)



