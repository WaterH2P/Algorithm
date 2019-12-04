# Every house in the colony has at most one pipe going into it and at most one pipe going out of it. 
# Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof 
# and every house with only an incoming pipe and no outgoing pipe gets a tap. 
# Find the efficient way for the construction of the network of pipes.

for _ in range(int(input().strip())):
    n, p = map(int, input().strip().split())
    pipes = []
    for i in range(p):
        a, b, d = map(int, input().strip().split())
        pipes.append([a, b, d])
    # 管道拼接
    i = 0
    while i < len(pipes):
        pipe1 = pipes[i]
        for j in range(len(pipes)):
            if j == i:
                continue
            pipe2 = pipes[j]
            isConnected = False
            if pipe1[0] == pipe2[1]:
                pipe2[1] = pipe1[1]
                isConnected = True
            elif pipe1[1] == pipe2[0]:
                pipe2[0] = pipe1[0]
                isConnected = True
            if isConnected:
                pipe2[2] = min(pipe1[2], pipe2[2])
                pipes.pop(i)
                i = -1
                break
        i += 1
    pipes.sort(key=lambda x: x[0])
    print(len(pipes))
    for pipe in pipes:
        print(*pipe, sep=' ')