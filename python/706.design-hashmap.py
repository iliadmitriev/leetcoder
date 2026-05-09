class MyHashMap:

    def __init__(self):
        self.size = 2048
        self.data = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.data[hash(key) % self.size]):
            if k == key:
                self.data[hash(key) % self.size][i] = (key, value)
                return

        self.data[hash(key) % self.size].append((key, value))

    def get(self, key: int) -> int:
        for key1, value in self.data[hash(key) % self.size]:
            if key1 == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        for i, (key1, value) in enumerate(self.data[hash(key) % self.size]):
            if key1 == key:
                del self.data[hash(key) % self.size][i]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)