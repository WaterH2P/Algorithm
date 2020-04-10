# 作为一个程序员，修bug（补漏洞）是一项基本的工作。当你刚刚完成一个工作的时候，甲方说你的程序里面有n个bug。
# 但是你已经很累了，你希望第一天修x个bug,第二天修[x/k]个bug，第三天修[x/k2]个bug，以此类推，第n天修⌊x/k^(n-1) ⌋个bug，直到修不了bug为止。
# [x]的意思是x向下取整。在k大于1的时候，总有一天会修不了一个bug的。所以，你希望在这一天来临之前，修完所有的bug。
# 你要计算，你第一次至少要修多少个bug，即x的最小值为多少。

# 输入包含一行两个整数n , k 分别代表漏洞总数和题目中的参数k
# 输出包含一个数，即x的最小值

import sys

n, k = map(int, input().strip().split())
if n <= 2: sys.stdout.write(str(n))
else:
    l, r = 1, n
    while l < r:
        x = (l + r) // 2
        tmpn = n
        tmpx = x
        while tmpn > 0 and tmpx > 0:
            tmpn -= tmpx
            tmpx = tmpx // k
        if tmpn <= 0: r = x
        else: l = x + 1
    sys.stdout.write(str(l) + '\n')
            
