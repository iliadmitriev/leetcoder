from threading import Barrier

class Foo:
    def __init__(self):
        self.done_1 = Barrier(2)
        self.done_2 = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.done_1.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.done_1.wait()
        printSecond()
        self.done_2.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done_2.wait()
        printThird()