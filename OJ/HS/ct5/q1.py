for t in range(int(input())):
    n, p = map(int, input().split())
    pipes = []
    for _ in range(p):
        a, b, d = map(int, input().split())
        pipes.append((a, b, d))
