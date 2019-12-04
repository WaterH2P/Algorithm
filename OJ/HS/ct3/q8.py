from itertools import groupby
for t in range(int(input())):
    arr = input()
    string = ''
    for i in range(26):
        if arr.find(chr(ord('A')+i)) != -1:
            string += chr(ord('A')+i)
    length, i = len(string), 0
    if length == 0:
        continue
    if length == 1:
        print(string)
        continue
    flag = [0 for i in range(length)]
    while i < length-1:
        flag[i] = ord(string[i+1]) - ord(string[i])
        i += 1
    lens = dict()
    i, max_offset = 0, 0
    while i < length - 1:
        offset = 1
        while i+offset < length - 1:
            if flag[i] == flag[i+offset]:
                offset += 1
            else:
                break
        lens[i], max_offset = offset, max(max_offset, offset)
        i += offset
    cans = []
    for i, offset in lens.items():
        if offset == max_offset:
            cans.append(i)
    print(string, cans)
    max_start = max([string[can] for can in cans])
    max_sum_cans = []
    for can in cans:
        if string[can] == max_start:
            max_sum_cans.append(can)
    min_gap = min([flag[can] for can in max_sum_cans])
    min_gap_cans = []
    for can in max_sum_cans:
        if flag[can] == min_gap:
            min_gap_cans.append(can)
    res = []
    for can in min_gap_cans:
        res.append(list(reversed(string[can:can+max_offset+1])))
    stringfied_res = []
    for lis in res:
        stringfied_res.append(''.join(lis))
    for _ in stringfied_res:
        print(_)