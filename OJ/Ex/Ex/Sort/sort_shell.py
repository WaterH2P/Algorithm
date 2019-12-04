# 实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），打印排序结果，注意不一定是最终排序结果！

for _ in range(int(input().strip())):
    nums = list(map(int, input().strip().split(' ')))
    diss = list(map(int, input().strip().split(' ')))
    for dis in diss:
        for i in range(dis):
            nums2 = []
            j = i
            while j < len(nums):
                nums2.append(nums[j])
                j += dis
            nums2.sort()
            j = i
            while j < len(nums):
                nums[j] = nums2.pop(0)
                j += dis
    print(*nums, sep=' ')