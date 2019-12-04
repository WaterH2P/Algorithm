pieces = []


def cover(size, sx, sy, x, y):
    if size == 1:
        return
    si = size // 2
    piece = []
    # (x, y) 在左上
    if x < si and y < si:
        cover(si, sx, sy, x, y)
    else:
        piece.append((sx + si - 1, sy + si - 1))
        cover(si, sx, sy, sx + si - 1, sy + si - 1)
    # (x, y) 在右上
    if x < si and y >= si:
        cover(si, sx, sy + si, x, y)
    else:
        piece.append((sx + si - 1, sy + si))
        cover(si, sx, sy + si, sx + si - 1, sy + si)
    # (x, y) 在左下
    if x >= si and y < si:
        cover(si, sx + si, sy, x, y)
    else:
        piece.append((sx + si, sy + si - 1))
        cover(si, sx + si, sy, sx + si, sy + si - 1)
    # (x, y) 在右下
    if x >= si and y >= si:
        cover(si, sx + si, sy + si, x, y)
    else:
        piece.append((sx + si, sy + si))
        cover(si, sx + si, sy + si, sx + si, sy + si)
    print(piece)
    pieces.append(piece)


for t in range(int(input())):
    n, x, y = map(int, input().split())
    query = tuple(map(int, input().split()))
    pieces = []
    cover(2 ** n, 0, 0, x, y)
    target = []
    for piece in pieces:
        if query in piece:
            target = piece
            break
    pos = target.index(query)
    res = []
    for idx, val in enumerate(target):
        if idx != pos:
            res.append(' '.join(str(_) for _ in val))
    print(*res, sep=',')
