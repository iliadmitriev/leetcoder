class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        pre = list(itertools.accumulate(stones))
        f = [0] * n
        f[n - 1] = pre[n - 1]

        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])

        return f[1]
