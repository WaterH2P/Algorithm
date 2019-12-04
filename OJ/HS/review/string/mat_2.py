# 无限递归字符串查询
inf = '12345$54321'

def find(pos):
  if pos <= 11:
    return inf[pos-1]
  L, step = 5, 1
  while L < pos:
    L = L*2 + step
    step += 1
  left = (L - step + 1) // 2
  if left < pos < left+step:
    return '$'
  return find(pos-left-step+1)

for t in range(int(input())):
  print(find(int(input())))

