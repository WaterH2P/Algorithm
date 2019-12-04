# 格子里的整数
for t in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().strip().split(' ')]
    V = len(arr)
    edge_list = []
    for i in range(V):
        # not at leftside
        if i%N != 0:
            edge_list.append([(i, i-1), arr[i-1]])
        # not at rightside
        if (i+1)%N != 0:
            edge_list.append([(i, i+1), arr[i+1]])
        # not at upside
        if (i-N) >= 0:
            edge_list.append([(i, i-N), arr[i-N]])
        # not at downside
        if (i+N) < (N*N):
            edge_list.append([(i, i+N), arr[i+N]])
    
    dist = dict()
    dist[0] = arr[0]
    # par = dict()
    # par[0] = None
    for i in range(1, V):
        dist[i] = float('inf')
    
    change = True
    ite = 0
    while ite < (V-1) and change:
        change = False
        for edge, wt in edge_list:
            u, v = edge            
            if dist[v] > (dist[u] + wt):
                dist[v] = dist[u] + wt
                # par[v] = u
                change = True
        ite += 1
        
    print(dist[V-1])
    
    # Print the path to (N-1, N-1)
    # node = V - 1
    # while node is not None:
    #     print(node, end='<-')
    #     node = par[node]
    # print(None)
    
    
    
    
    
    