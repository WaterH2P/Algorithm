from collections import Counter
for u in range(int(input())):
    l, arr, res = int(input()), list(map(int, input().split())), list()
    for v, f in sorted(Counter(arr).items(), key=lambda a: (-a[1], a[0])):
        [res.append(v) for i in range(f)]
    print(*res)
