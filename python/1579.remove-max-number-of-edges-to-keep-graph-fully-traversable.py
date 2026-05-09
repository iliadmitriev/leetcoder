from typing import List


class DisjointSet:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def join(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_y] = root_x
        return True

    def count(self):
        return len({self.find(x) for x in self.parent})


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob, both = [], [], []
        for typ, src, dst in edges:
            if typ == 1:
                alice.append((typ, src - 1, dst - 1))
            elif typ == 2:
                bob.append((typ, src - 1, dst - 1))
            else:
                both.append((typ, src - 1, dst - 1))

        counter = 0
        set_bob, set_alice = DisjointSet(n), DisjointSet(n)
        for typ, src, dst in both:
            res = set_alice.join(src, dst)
            res = set_bob.join(src, dst)
            if not res:
                counter += 1

        for typ, src, dst in alice:
            if not set_alice.join(src, dst):
                counter += 1

        for typ, src, dst in bob:
            if not set_bob.join(src, dst):
                counter += 1

        if set_alice.count() == 1 and set_bob.count() == 1:
            return counter

        return -1

