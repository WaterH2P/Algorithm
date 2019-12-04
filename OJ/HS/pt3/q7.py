num = 0


def find_ins(edges):
    in_nodes, out_nodes = set(), set()
    for edge in edges:
        in_nodes.add(edge[1])
        out_nodes.add(edge[0])
    return out_nodes - in_nodes


def remove_node(edges, node):
    res = []
    for edge in edges:
        if edge[0] != node and edge[1] != node:
            res.append(edge)
    return res


def recurve(edges):
    global num
    if len(edges) == 1:
        num += 1
    in_nodes = find_ins(edges)
    for in_node in in_nodes:
        recurve(remove_node(edges, in_node))


for t in range(int(input())):
    edges = [tuple(_.split()) for _ in input().split(',')]
    num = 0
    recurve(edges)
    print(num)


