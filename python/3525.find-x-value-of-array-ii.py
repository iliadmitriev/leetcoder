import math

MAXK = 6


class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.k = k
        self.n = len(nums)

        size = 2 << int(math.ceil(math.log2(self.n)))
        self.data = [[0] * MAXK for _ in range(size)]

        self._build(nums, 1, 0, self.n - 1)

    def _mk_node(self, o: int, value: int):
        for i in range(MAXK):
            self.data[o][i] = 0

        r = value % self.k
        self.data[o][r] = 1
        self.data[o][self.k] = r

    def _merge_node(self, left, right, res):
        for i in range(MAXK):
            res[i] = 0

        k = self.k

        mul_L = left[k]
        mul_R = right[k]
        res[k] = (mul_L * mul_R) % k

        # case 1: entirely within the left interval
        for x in range(k):
            res[x] = left[x]

        # case 2: contain the entire left interval
        # followed partial right
        for x in range(k):
            res[(mul_L * x) % k] += right[x]

    def _build(self, nums: list[int], o, l, r):
        if l == r:
            self._mk_node(o, nums[l])
            return

        m = (l + r) // 2
        self._build(nums, o * 2, l, m)
        self._build(nums, o * 2 + 1, m + 1, r)

        self._merge_node(self.data[o * 2], self.data[o * 2 + 1], self.data[o])

    def _update(self, o, l, r, index, value):
        if l == r:
            self._mk_node(o, value)
            return

        m = (l + r) // 2

        if index <= m:
            self._update(o * 2, l, m, index, value)
        else:
            self._update(o * 2 + 1, m + 1, r, index, value)

        self._merge_node(self.data[o * 2], self.data[o * 2 + 1], self.data[o])

    def _query(self, o, l, r, L, R):
        # if current request [L, R] covers the whole node child space [l, r]
        if L <= l and r <= R:
            return self.data[o]

        m = (l + r) // 2

        # if current requst [L,R] covers only the node's left child space [l, m]
        if R <= m:
            return self._query(o * 2, l, m, L, R)
        # if current request [L,R] covers only the node's right child space [m+1, r]
        if L > m:
            return self._query(o * 2 + 1, m + 1, r, L, R)

        left = self._query(o * 2, l, m, L, R)
        right = self._query(o * 2 + 1, m + 1, r, L, R)

        res = [0] * MAXK
        self._merge_node(left, right, res)
        return res

    def update(self, index: int, value: int):
        self._update(1, 0, self.n - 1, index, value)

    def query(self, L: int, R: int):
        return self._query(1, 0, self.n - 1, L, R)


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        seg = SegmentTree(nums, k)
        res = []

        for index, value, start, x in queries:
            seg.update(index, value)
            pre = seg.query(start, n - 1)
            res.append(pre[x])

        return res
