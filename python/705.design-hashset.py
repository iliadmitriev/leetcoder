class MyHashSet:
    
    INIT_BUCKET_SIZE = 3000

    def __init__(self):
        self.load = 0
        self.bucket_size = self.INIT_BUCKET_SIZE
        self.storage = [[] for _ in range(self.bucket_size)]
        
    def _get_bucket(self, key):
        return self.storage[key % self.bucket_size]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            bucket = self._get_bucket(key)
            self.load += 1
            bucket.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            bucket = self._get_bucket(key)
            self.load -= 1
            bucket.remove(key)

    def contains(self, key: int) -> bool:
            bucket = self._get_bucket(key)
            return key in bucket
    
    def _check_load(self):
        return self.load / self.bucket_size


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)