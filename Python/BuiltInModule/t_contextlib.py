from contextlib import contextmanager, closing
from urllib.request import urlopen

# with 语句允许我们非常方便地使用资源，而不必担心资源没有关闭
with open('./test.txt', 'r') as f :
    print(f.read())

# https://www.liaoxuefeng.com/wiki/1016959663602400/1115615597164000
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

# @contextmanager 这个 decorator 接受一个 generator，
# 用 yield 语句把 with ... as var 把变量输出出去，
# with 语句就可以正常地工作了
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# 如果一个对象没有实现上下文，我们就不能把它用于 with 语句。
# 这个时候，可以用 closing() 来把该对象变为上下文对象。
# 例如，用 with 语句使用 urlopen()
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)