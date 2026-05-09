class UF:
    __slots__ = ("parent",)
    base = ord("a")

    def __init__(self):
        self.parent = list(range(26))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if px > py:
            px, py = py, px

        self.parent[py] = px

    def union_char(self, x, y):
        self.union(ord(x) - self.base, ord(y) - self.base)

    def find_char(self, x):
        return chr(self.base + self.find(ord(x) - self.base))


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UF()
        for a, b in zip(s1, s2):
            uf.union_char(a, b)

        return "".join(uf.find_char(c) for c in baseStr)

