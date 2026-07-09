class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:
        m = len(queries)
        res = [False] * m
        group = 0
        groups = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group += 1

            groups[i] = group

        for j, (u, v) in enumerate(queries):
            res[j] = groups[u] == groups[v]

        return res
