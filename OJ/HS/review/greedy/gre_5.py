# 路上的球
for t in range(int(input())):
    m, n = map(int,input().split())
    first  = list(map(int,input().split()))
    second = list(map(int,input().split()))

    # find intersections
    intersection = [[0, 0]]
    f, s = 0, 0
    while f<m and s<n:
        if first[f] > second[s]:
            s += 1
        elif first[f] < second[s]:
            f += 1
        else:
            try:
                if first[f+1] == first[f]:
                    f += 1
                    continue
                if second[s+1] == second[s]:
                    s += 1
                    continue
            except:
                pass
            intersection.append([f, s])
            f += 1
            s += 1
    intersection.append([m, n])
    
    # 根据交点将两个数组切片, 每一片取 sum 大的
    count, f, s = 0, 0, 0
    for i in range(len(intersection)-1):
        sec_head = intersection[i]
        sec_tail = intersection[i+1]
        fsum = sum(first[sec_head[0]:sec_tail[0]])
        ssum = sum(second[sec_head[1]:sec_tail[1]])
        count += max(fsum, ssum)
    print(count)