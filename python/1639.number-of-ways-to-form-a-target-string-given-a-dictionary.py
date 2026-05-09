from collections import Counter
from functools import cache


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        n, p, m = len(target), len(words), len(words[0])
        MOD = int(1e9 + 7)
        counts = []

        for j in range(m):
            cnt = Counter()
            for k in range(p):
                cnt[words[k][j]] += 1
            counts.append(cnt)

        @cache
        def dfsNumWays(i: int, j: int) -> int:
            if i == n:
                return 1

            if m - j < n - i:
                return 0

            ways = 0
            # take
            if target[i] in counts[j]:
                ways += dfsNumWays(i + 1, j + 1) * counts[j][target[i]]

            # skip
            ways += dfsNumWays(i, j + 1)

            return ways % MOD

        return dfsNumWays(0, 0)

