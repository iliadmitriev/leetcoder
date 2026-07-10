class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:
        m = len(queries)
        res = [0] * m
        # sorted nodes by weights
        sp = sorted((w, v) for v, w in enumerate(nums))

        # node -> sorted index 
        idx = [0] * n
        for i, (_, v) in enumerate(sp):
            idx[v] = i

        # binary uplifting
        LOG = 18
        ds = [[0] * LOG for _ in range(n)]

        r = 0 # component range
        for i in range(n):
            if r < i:
                r = i

            while (
                r + 1 < n
                and sp[r + 1][0] - sp[r][0] <= maxDiff
                and sp[r + 1][0] - sp[i][0] <= maxDiff
            ):
                r += 1

            ds[i][0] = r

        for j in range(1, LOG):
            for i in range(n):
                half = ds[i][j - 1]
                ds[i][j] = ds[half][j - 1]

        for i, (u, v) in enumerate(queries):
            if u == v:
                res[i] = 0
                continue

            # a and b sorted indices of u and v (a < b)
            a, b = idx[u], idx[v]
            a, b = min(a, b), max(a, b)

            # start from a and make a binary jumps to b
            cur, steps = a, 0
            for j in range(LOG - 1, -1, -1):
                if ds[cur][j] < b:
                    cur = ds[cur][j]  # lift
                    steps += 1 << j  # add steps 2^j

            res[i] = steps + 1 if ds[cur][0] >= b else -1

        return res
