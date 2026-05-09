from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_lock=Lock()
        self.odd_lock=Lock()
        self.zero_lock=Lock()
        # lock even and odd locks
        # for zero have to be the first
        self.even_lock.acquire()
        self.odd_lock.acquire()
        
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            # release odd if i is odd
            # otherwise even
            if i % 2:
                self.odd_lock.release()
            else:
                self.even_lock.release()
                
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
            
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
