class UF:
    def __init__(self, size: int) -> None:
        self._size = size
        self._par = list(range(size))
        self._rank = [1] * size

    def find(self, x: int) -> int:
        while x != self._par[x]:
            self._par[x] = self._par[self._par[x]]
            x = self._par[x]
        return self._par[x]

    def join(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self._rank[py] > self._rank[px]:
            px, py = py, px

        self._rank[px] += self._rank[py]
        self._rank[py] = 0
        self._par[py] = self._par[px]
        self._size -= 1
        return True

    def __len__(self) -> int:
        return self._size


def factors(num: int):
    while num % 2 == 0:
        yield 2
        num //= 2

    lim = 1 + isqrt(num - 1)
    for i in range(3, lim + 1, 2):
        while num % i == 0:
            yield i
            num //= i

    if num > 2:
        yield num


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UF(len(nums))

        factors_cache = {}
        for i, num in enumerate(nums):
            for k in factors(num):
                if k in factors_cache:
                    uf.join(i, factors_cache[k])
                else:
                    factors_cache[k] = i

        return len(uf) == 1