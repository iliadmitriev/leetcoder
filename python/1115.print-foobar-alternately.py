from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = (Lock(), Lock())
        self.lock[1].acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock[0].acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock[1].release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock[1].acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock[0].release()
