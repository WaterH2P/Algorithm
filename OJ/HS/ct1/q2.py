t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    nums = list(map(int, input().split()))
    indexed_nums = [*enumerate(nums)]
    indexed_nums.sort(key=lambda a: a[1])
    visited = {i: False for i in range(n)}
    count = 0
    for i in range(n):
        if visited[i] or i == indexed_nums[i][0]:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = indexed_nums[j][0]
            cycle_size += 1
        if cycle_size > 0:
            count += (cycle_size - 1)
    print(count)

