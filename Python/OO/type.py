
# 动态创建类
def fn(self, name='world'):
    print('Hello %s' % name)

# 创建 Hello class
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()