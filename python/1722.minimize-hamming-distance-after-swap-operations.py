import collections


class UF:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x

    def join(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        self.par[px] = py
        return True

    def comp(self) -> list[int]:
        n = len(self.par)
        res = [0] * n

        for i in range(n):
            res[i] = self.find(i)

        return res


class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], allowedSwaps: list[list[int]]
    ) -> int:
        n = len(source)
        uf = UF(n)

        for a, b in allowedSwaps:
            _ = uf.join(a, b)

        swaps = uf.comp()
        no_match = 0
        groups = collections.defaultdict(lambda: collections.defaultdict(int))

        for i, s in enumerate(swaps):
            groups[s][source[i]] += 1

        for i, s in enumerate(swaps):
            if target[i] in groups[s] and groups[s][target[i]] > 0:
                groups[s][target[i]] -= 1
            else:
                no_match += 1

        return no_match
