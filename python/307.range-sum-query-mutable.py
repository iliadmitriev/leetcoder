class BinaryIndexTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


class NumArray:
    def __init__(self, nums: list[int]):
        self.cur = nums
        self.bit = BinaryIndexTree(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i, num)

    def update(self, index: int, val: int) -> None:
        dalta = val - self.cur[index]
        self.bit.update(index, dalta)
        self.cur[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right) - self.bit.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)