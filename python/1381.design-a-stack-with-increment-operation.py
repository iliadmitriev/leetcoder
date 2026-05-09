

class CustomStack:

    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.top = 0
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize  # suffix increment

    def push(self, x: int) -> None:
        if self.top == self.capacity:
            return

        self.stack[self.top] = x
        self.inc[self.top] = 0
        self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            return -1

        self.top -= 1
        inc = self.inc[self.top]
        x = self.stack[self.top] + inc

        if self.top > 0:
            self.inc[self.top - 1] += inc

        return x

    def increment(self, k: int, val: int) -> None:
        k = min(k - 1, self.top - 1)
        self.inc[k] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)