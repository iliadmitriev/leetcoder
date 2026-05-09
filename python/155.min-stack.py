class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, val: int) -> None:
        if self._min is None or self._min > val:
            self._min = val
        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if len(self._stack):
            self._min = min(self._stack)
        else:
            self._min = None
        return val

    def top(self) -> int:
        if len(self._stack):
            return self._stack[-1]
        return 0

    def getMin(self) -> int:
        return self._min



# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
