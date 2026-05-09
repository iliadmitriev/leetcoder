class RandomizedSet:

    def __init__(self):
        self.data = list()
        self.indices = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        # instead of deleting - repalce deleting element
        # with last element 
        self.indices[self.data[-1]] = self.indices[val]
        self.data[self.indices[val]] = self.data[-1]

        # and throw away last element
        self.indices.pop(val)
        self.data.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()