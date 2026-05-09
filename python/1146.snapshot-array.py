class SnapshotArray:

    def __init__(self, length: int):
        # current snap
        self.snap_id = 0
        # tuples (snap_id, value)
        self.data = [[(0, 0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        data = self.data[index]
        if data[-1][0] == self.snap_id:
            data[-1] = (self.snap_id, val)
        else:
            data.append((self.snap_id, val))

    def snap(self) -> int:
        snap_id = self.snap_id
        self.snap_id += 1
        return snap_id
        
    def get(self, index: int, snap_id: int) -> int:
        data = self.data[index]
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return data[right][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)