import sys
if __name__ == "__main__":
    for i in range(int(sys.stdin.readline().strip())):
        n = int(sys.stdin.readline().strip())
        lengths = list(map(int, sys.stdin.readline().strip().split()))
        weights = list(map(int, sys.stdin.readline().strip().split()))
        res = [[[lengths[0], weights[0]]]]
        for i in range(1, n):
            isInsert = False
            for j in range(len(res)):
                lws = res[j]
                for k in range(len(lws)):
                    l, w = lws[k]
                    if lengths[i] <= l and weights[i] <= w:
                        res[j].insert(k, [lengths[i], weights[i]])
                        isInsert = True
                        break
                    if (lengths[i] > l and weights[i] < w) or (lengths[i] < l and weights[i] > w): break
                    if lengths[i] >= l and weights[i] >= w and k == len(lws) - 1:
                        res[j].append([lengths[i], weights[i]])
                        isInsert = True
                        break
                if isInsert: break
            if not isInsert: res.append([[lengths[i], weights[i]]])
        print(len(res))