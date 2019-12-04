from itertools import combinations
for t in range(int(input())):
    a, b = input(), input()
    n = min(len(a), len(b))
    res = list()
    while n > 0:
        combs_a, combs_b = list(combinations(a, n)), list(combinations(b, n))
        n -= 1
        # count = 0
        # [res.append(''.join(comb_a)) for comb_a in combs_a for comb_b in combs_b if comb_a == comb_b]
        # print(len([1 for i in combs_a for b in combs_b]))
        for comb_a in combs_a:
            tmp_a = ''.join(comb_a)
            for comb_b in combs_b:
                tmp_b = ''.join(comb_b)
                # count += 1
                # print(tmp_a, tmp_b)
                if tmp_a == tmp_b:
                    # print(tmp_a)
                    res.append(tmp_a)
        # print(n, count)
        if len(res):
            break
    # print(res)
    if len(res):
        res = [_ for _ in set(res)]
        res.sort()
        for _ in res:
            print(_)

