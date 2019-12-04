def lis(a):
    cans = list()
    for item in a:
        inserted, tmp_list = False, list()
        for can in cans:
            if item >= can[-1]:
                tmp_list.append(can + [item])
                inserted = True
        cans.extend(tmp_list) if inserted else cans.append([item])
    return [list(t) for t in set(tuple(_) for _ in cans)]


for u in range(int(input())):
    in_arr = list(map(int, input().split()))
    n, res = len(in_arr), list()
    for sep in range(1, n):
        ls, rs = lis(in_arr[:sep]), lis(in_arr[:sep-1:-1])
        [res.append(l + r[::-1]) for l in ls for r in rs]
    distinct_res = [list(t) for t in set(tuple(_) for _ in res)]
    max_len = len(max(distinct_res, key=lambda a: len(a)))
    result = sorted(filter(lambda a: len(a) == max_len, distinct_res), key=lambda a: ' '.join(str(i) for i in a))
    for line in result:
        print(*line)

