# 管道网络
def find_pipe(start, pipes):
    for pipe in pipes:
        if pipe[0] == start:
            return pipe

def find_next(cur, pipes):
    for pipe in pipes:
        if pipe[0] == cur[1]:
            return pipe

for t in range(int(input())):
    n, p = map(int, input().split())
    pipes = []
    for _ in range(p):
        a, b, d = map(int, input().split())
        pipes.append((a, b, d))
    inp_set = set([pipe[0] for pipe in pipes])
    out_set = set([pipe[1] for pipe in pipes])
    inps = list(inp_set - out_set)
    outs = list(out_set - inp_set)
    res = []

    for inp in inps:
        cur = find_pipe(inp, pipes)
        minimum = cur[2]
        itr = cur
        while find_next(itr, pipes):
            itr = find_next(itr, pipes)
            minimum = min(minimum, itr[2])
        res.append((cur[0], itr[1], minimum))
    
    print(len(res))
    res.sort()
    [print(*_) for _ in res]
