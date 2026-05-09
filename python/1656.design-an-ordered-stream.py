class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.size = n + 1
        self.data = [None] * (self.size)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        start, end = self.ptr, self.ptr
        while end < self.size and self.data[end] is not None:
            end += 1
        self.ptr = end
        return self.data[start:end]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)