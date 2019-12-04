from itertools import permutations
for t in range(int(input())):
    n, arr = int(input()), input()
    ls = [tuple(map(int, _.split())) for _ in arr.split(sep=',')]
    matrix = [[0 for i in range(n)] for j in range(n)]
    for pair in ls:
        matrix[pair[0]-1][pair[1]-1] = pair[2]
    order = list(range(n))
    cur_min = sum([matrix[idx][val] for idx, val in enumerate(order)])
    for comb in permutations(order, n):
        cur_min = min(cur_min, sum([matrix[idx][val] for idx, val in enumerate(comb)]))
    sol = []
    for comb in permutations(order, n):
        if sum([matrix[idx][val] for idx, val in enumerate(comb)]) == cur_min:
            sol.append(comb)
    sol.sort(reverse=True)
    res = []
    for _ in sol:
        res.append(' '.join(str(i+1) for i in _))
    print(*res, sep=',')
