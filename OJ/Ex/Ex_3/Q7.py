# 求解拓扑排序解的个数
for _ in range(int(input().strip())):
    edges = [item.split(' ') for item in input().strip().split(',')]
    points = {}
    for edge in edges:
        if edge[0] not in points:
            points[edge[0]] = {
                'in': 0,
                'outs': [edge[1]]
            }
        else:
            if edge[1] not in points[edge[0]]['outs']:
                points[edge[0]]['outs'].append(edge[1])
        if edge[1] not in points:
            points[edge[1]] = {
                'in': 1,
                'outs': []
            }
        else:
            points[edge[1]]['in'] += 1
    existZeroIn = True
    count = 1
    while existZeroIn:
        existZeroIn = False
        zeroIns = []
        for item in points:
            if points[item]['in'] == 0:
                existZeroIn = True
                if item not in zeroIns:
                    zeroIns.append(item)
        if len(zeroIns) > 0:
            count *= len(zeroIns)
        for zeroIn in zeroIns:
            outs = points.pop(zeroIn)['outs']
            for item in points:
                if item in outs:
                    points[item]['in'] -= 1
    print(count)
