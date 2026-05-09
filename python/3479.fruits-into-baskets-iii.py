import math


class MaxSegmentTree:
    """Maximum segment tree implementation."""

    def __init__(self, arr: list[int]):
        n = len(arr)
        # size of complete binary tree (rightmost leaves zerofilled)
        size = 1 << n.bit_length()
        tree = [0] * (2 * size)

        tree[size : size + n] = arr

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        self.size = size
        self.tree = tree

    def update(self, i: int, x: int) -> None:
        i += self.size
        self.tree[i] = x
        i //= 2

        while i > 0:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def first_ge_than(self, x: int) -> int:
        """Find the first index i such that tree[i] <= x.

        Returns i if there is such index, -1 otherwise.
        """
        i = 1

        if self.tree[i] < x:
            return -1

        while i < self.size:
            if self.tree[2 * i] >= x:
                i = 2 * i
            else:
                i = 2 * i + 1

        return i - self.size


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        tree = MaxSegmentTree(baskets)
        count = 0

        for fruit in fruits:
            j = tree.first_ge_than(fruit)
            if j == -1:
                count += 1
                continue

            tree.update(j, 0)

        return count

    def numOfUnplacedFruitsV1(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(baskets)  # number of baskets
        m = int(math.sqrt(n))  # number of baskets in bucket
        k = (n + m - 1) // m  # number of buckets (ceil(n / m))
        unplaced = 0
        maxRng = [0] * k

        for i in range(n):
            maxRng[i // m] = max(maxRng[i // m], baskets[i])

        for fruit in fruits:
            j = -1

            for i in range(k):
                if fruit <= maxRng[i]:
                    j = i
                    break

            if j == -1:
                unplaced += 1
                continue

            # update maxRng, remove target from bucket maximum
            # and calculate new maximum
            basMax = 0
            removed = False
            for i in range(j * m, min((j + 1) * m, n)):
                if not removed and baskets[i] >= fruit:
                    baskets[i] = 0
                    removed = True

                if baskets[i] > basMax:
                    basMax = baskets[i]

            maxRng[j] = basMax

        return unplaced

