from collections import namedtuple, deque, OrderedDict, ChainMap, Counter
import os, argparse

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# deque 是为了高效实现插入和删除操作的双向列表
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('y')
print(q)


# 保持 Key 的顺序，可以用 OrderedDict
# OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)


# ChainMap 可以把一组 dict 串起来并组成一个逻辑上的 dict。
# ChainMap 本身也是一个 dict，但是查找的时候，会按照顺序在内部的 dict 依次查找。
# 构造缺省参数:
defaults = {
    'color' : 'red',
    'user'  : 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


# Counter是一个简单的计数器
c = Counter()
for ch in 'programming' :
    c[ch] += 1
print(c)