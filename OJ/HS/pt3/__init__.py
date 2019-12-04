inf = '12345'
step = 0


def find(pos):
    global inf, step
    if pos < len(inf):
        return inf[pos]
    step += 1
    inf = inf + '$' * step + inf[::-1]
    return find(pos)


for t in range(int(input())):
    print(find(int(input())-1))
