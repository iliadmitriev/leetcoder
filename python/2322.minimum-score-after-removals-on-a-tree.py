import functools
import operator
import sys


class Solution:
    @staticmethod
    def calc(v1: int, v2: int, v3: int):
        return max(v1, v2, v3) - min(v1, v2, v3)

    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total = functools.reduce(operator.xor, nums)
        res = sys.maxsize  # infinity

        def dfs2(x: int, f: int, oth: int, anc: int) -> int:
            son = nums[x]

            for y in adj[x]:
                if y == f:
                    continue
                son ^= dfs2(y, x, oth, anc)

            if f == anc:
                return son

            nonlocal res
            res = min(res, self.calc(oth, son, total ^ son ^ oth))

            return son

        def dfs(x: int, p: int) -> int:
            """
            x: current node
            p: parent
            """
            son = nums[x]

            for y in adj[x]:
                if y == p:
                    continue
                son ^= dfs(y, x)

            for y in adj[x]:
                if y == p:
                    dfs2(y, x, son, x)

            return son

        dfs(0, -1)

        return res

