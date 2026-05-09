class FenwickTree:
    def __init__(self, n):
        self.data = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.data):
            self.data[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        count = 0
        n = len(nums1)

        pos2 = {v: i for i, v in enumerate(nums2)}
        reverseIndexMapping = {pos2[v]: i for i, v in enumerate(nums1)}

        ft = FenwickTree(n)

        for idx in range(n):
            pos = reverseIndexMapping[idx]
            left = ft.query(pos)
            ft.update(pos, 1)
            right = n - 1 - pos - (idx - left)

            count += left * right

        return count

