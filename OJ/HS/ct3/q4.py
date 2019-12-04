import re
for t in range(int(input())):
    txt, pattern = input().split(sep=',')
    n, m = len(txt), len(pattern)
    print(*[m.start() for m in re.finditer(re.compile(r'(?='+pattern+')'), txt)])
    # i = 0
    # res = []
    # while i < n:
    #     if txt[i] == pattern[0]:
    #         offset = 1
    #         while offset < m and i + offset < n:
    #             if txt[i + offset] != pattern[offset]:
    #                 break
    #             offset += 1
    #         if offset == m:
    #             res.append(i)
    #     i += 1
    # print(*res)



