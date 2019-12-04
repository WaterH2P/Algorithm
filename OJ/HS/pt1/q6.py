for u in range(int(input())):
    raw, k = list(map(int, input().split())), int(input())
    print(len([(i, j) for index, i in enumerate(raw) for j in [k-l for l in raw[index+1:]] if i == j]))
    # flag = [(k-i) for i in raw]
    # count = 0
    # for index, i in enumerate(raw):
    #     for j in flag[index+1:]:
    #         if i == j:
    #             count += 1
    # print(count)


