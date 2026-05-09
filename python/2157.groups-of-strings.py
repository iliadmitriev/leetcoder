class DSU:
    def __init__(self, size: int):
        self._parent = list(range(size))
        self._rank = list(repeat(1, size))

    def find(self, x: int) -> int:
        while x != self._parent[x]:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def join(self, x: int, y: int) -> bool:
        par_x, par_y = self.find(x), self.find(y)

        if par_x == par_y:
            return False

        if self._rank[par_y] > self._rank[par_x]:
            par_x, par_y = par_y, par_x

        self._parent[par_y] = self._parent[par_x]
        self._rank[par_x] += self._rank[par_y]
        self._rank[par_y] = 0
        return True

    def components(self):
        count = 0
        lengths = [0] * len(self._parent) 
        for i in range(len(self._parent)):
            key = self.find(i)
            if key == i:
                count += 1
            lengths[key] += 1
        return count, max(lengths)


def mask(s: str) -> int:
    res = 0
    for ch in s:
        res |= 1 << (ord(ch) - 97)
    return res


def connected(x: int) -> Iterator[int]:
    for i in range(26):
        if x & (1<<i) != 0:
            yield x ^ (1<<i)


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # init disjoint set union
        dsu = DSU(len(words))

        cache = {}

        for i, word in enumerate(words):
            msk = mask(word)
            # put the word mask to cache along with its index
            j = cache.setdefault(msk, i)
            # check if it has already been added to cache with different index
            # then it's needed to connect these indices with same words
            if i != j:
                dsu.join(i, j)
                
            # check all of the similar masks
            for key in connected(mask(word)):
                if key not in cache:
                    cache[key] = i
                else:
                    dsu.join(i, cache[key])

        # return number of groups and size of largest group
        return dsu.components()

