n = int(input().strip())
for i in range(n):
    nums = [int(k) for k in input().strip()]
    # diff 存储 sum(l) - sum(r)
    diff_l = [[], []]
    diff_r = [[], []]
    maxLen = 0
    for k in nums:
        for j in range(len(diff_l[0])):
            if k == diff_l[0][j]:
                maxLen = max(maxLen, diff_l[1][j] + 1)
        for j in range(len(diff_r[0])):
            if k == diff_r[0][j]:
                maxLen = max(maxLen, diff_r[1][j] + 1)

        for j in range(len(diff_r[0])):
            diff_r[0][j] -= k
            diff_r[1][j] += 1
        diff_r[0].append(-k)
        diff_r[1].append(1)

        for j in range(len(diff_l[0])):
            diff_r[0].append(diff_l[0][j] - k)
            diff_r[1].append(diff_l[1][j] + 1)
            diff_l[0][j] += k
            diff_l[1][j] += 1
        diff_l[0].append(k)
        diff_l[1].append(1)

    print(maxLen)