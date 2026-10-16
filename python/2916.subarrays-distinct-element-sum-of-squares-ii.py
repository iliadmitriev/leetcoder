class BinaryIndexTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self._tree1 = [0] * (size + 1)
        self._tree2 = [0] * (size + 1)

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    @staticmethod
    def _lowbit(index: int) -> int:
        return index & -index

    def _add(self, index: int, delta: int) -> None:
        value = delta * index
        index += 1

        while (index <= self.size):
            self._tree1[index] += delta
            self._tree2[index] += value
            index += self._lowbit(index)
    
    def _query(self, index: int) -> int:
        index += 1
        coef = index
        res = 0

        while index > 0:
            res += coef * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)

        return res


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = int(1e9) + 7
        
        res = 0
        cur = 0
        bit = BinaryIndexTree(n + 1)
        seen = {} # previous position of value

        for i, x in enumerate(nums):
            j = seen.get(x, -1) + 1 # left boundary
            
            q = bit.query(j, i)
            cur = (cur + 2 * q + i - j + 1) % MOD
            res = (res + cur) % MOD

            seen[x] = i
            bit.add(j, i, 1)

        return res


        