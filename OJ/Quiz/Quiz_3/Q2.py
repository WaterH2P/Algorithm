n = int(input().strip())
for z in range(n):
    s = input().strip()
    nums1 = list(map(int, input().strip().split(' ')))
    nums2 = list(map(int, input().strip().split(' ')))
    count = []
    for num in nums2:
        c = 0
        for i in nums1:
            if i % num == 0:
                c += 1
        count.append(str(c))
    output = ' '.join(count)
    print(output)