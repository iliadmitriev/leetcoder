class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        prefix = [0]
        cur = 0
        i = 0

        while n:
            if n & 1:
                cur += i
                prefix.append(cur)
            i += 1
            n >>= 1

        mod = int(1e9) + 7
        m = len(prefix)

        cache = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                cache[i][j] = pow(2, (prefix[j] - prefix[i]), mod)

        return [cache[a][b + 1] for a, b in queries]

