# 1115. 交替打印FooBar
# 两个不同的线程将会共用一个 FooBar 实例。
# 其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
# 请设计修改程序，以确保 "foobar" 被输出 n 次。


import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = threading.Semaphore(1)
        self.b = threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.f.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.b.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()