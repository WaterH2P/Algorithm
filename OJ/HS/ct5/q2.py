for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dep = list(map(int, input().split()))
    # arr.sort()
    # dep.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] < dep[j]:
            plat_needed += 1
            i += 1
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed -= 1
            j += 1
    print(result)
