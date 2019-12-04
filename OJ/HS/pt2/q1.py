def lis(a):
    cans = list()
    for item in a:
        inserted, tmp_list = False, list()
        for can in cans:
            if item[1] >= can[-1][1]:
                tmp_list.append(can + [item])
                inserted = True
        cans.extend(tmp_list) if inserted else cans.append([item])
    return [list(t) for t in set(tuple(_) for _ in cans)]


for t in range(int(input())):
    a, b = input(), input()
    pairs_list = list()
    for i in range(len(a)):
        tmp = list()
        for j in range(len(b)):
            if a[i] == b[j]:
                tmp.append((i, j))
        if len(tmp):
            if len(pairs_list):
                tmp_list = pairs_list
                pairs_list = list()
                for item in tmp:
                    for pairs in tmp_list:
                        pairs_list.append(pairs + [item])
            else:
                for item in tmp:
                    pairs_list.append([item])
    if not len(pairs_list):
        continue
    cans = list()
    for pairs in pairs_list:
        cans += lis(pairs)
    max_len = len(max(cans, key=lambda x: len(x)))
    possible_pairs = filter(lambda x: len(x) == max_len, cans)
    res = list()
    for res_pairs in possible_pairs:
        tmp = ''
        for (i, j) in res_pairs:
            tmp += a[i]
        res.append(tmp)
    res = [_ for _ in set(res)]
    res.sort()
    for _ in res:
        print(_)

