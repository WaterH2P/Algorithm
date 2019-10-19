def  map_record(n,c,w,v):
	# 初始化记录表
    record_map = [[0 for i in range(c+1)] for i in range(len(n)+1)]
    for i in range(1, len(n)+1) :
        # 应用状态转移函数填写记录表
        for j in range(1, c+1) :
            if j < w[i-1] :
                record_map[i][j] = record_map[i-1][j]
                print('if', record_map)
            else :
                record_map[i][j] = max(record_map[i-1][j],record_map[i-1][j-w[i-1]]+v[i-1])
                print('el', record_map)
    return record_map

def show(n,c,w,res):
    print('最大价值为：',res[len(n)][c])
    x = [False for i in range (len(n)+1)]
    j = c
    i = len(n)
    # 回溯
    while i >= 0 :
        if res[i][j] > res[i-1][j] :
            x[i] = True
            j -= w[i-1]
        i -= 1
    print('选择的物品为：')
    for i in range(len(n)+1) :
        if x[i] :
            print('第', i, '个,', end='')
    print('')

n = ['a','b','c','d']
c = 8
w = [2,4,5,3]
v = [5,4,6,2]
res = map_record(n,c,w,v)
show(n,c,w,res)