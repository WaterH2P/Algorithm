for _ in range(int(input().strip())):
    n, a, b = map(int, input().strip().split())
    ai = list(map(int, input().strip().split()))
    bi = list(map(int, input().strip().split()))
    dis = [0 for i in range(n)]
    # 记录 a 完成的 order
    aic = [0 for i in range(n)]
    # 记录 b 完成的 order
    bic = [0 for i in range(n)]
    ac, bc = 0, 0
    for i in range(n):
        dis[i] = abs(ai[i] - bi[i])
    for i in range(n):
        index = -1
        d = 999
        if ai[i] >= bi[i]:
            if ac < a:
                aic[i] = 1
                ac += 1
            else:
                # a's order 达到上限，寻找是否可以替换的 order
                for j in range(i):
                    if aic[j] == 1 and dis[j] < dis[i]:
                        if dis[j] < d:
                            d = dis[j]
                            index = j
                if index > -1:
                    aic[i] = 1
                    aic[index] = 0
                    bic[index] = 1
                else:
                    bic[i] = 1
        else:
            if bc < b:
                bic[i] = 1
                bc += 1
            else:
                # b's order 达到上限，寻找是否可以替换的 order
                for j in range(i):
                    if bic[j] == 1 and dis[j] < dis[i]:
                        if dis[j] < d:
                            d = dis[j]
                            index = j
                if index > -1:
                    bic[i] = 1
                    bic[index] = 0
                    aic[index] = 1
                else:
                    aic[i] = 1
    tip = 0
    for i in range(n):
        if aic[i] == 1:
            tip += ai[i]
        elif bic[i] == 1:
            tip += bi[i]
    print(tip)