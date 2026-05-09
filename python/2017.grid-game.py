class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        pre1, pre2 = grid[0].copy(), grid[1].copy()

        for i in range(1, n):
            pre1[i] += pre1[i - 1]
            pre2[i] += pre2[i - 1]

        res = float("inf")
        for i in range(n):
            top = pre1[-1] - pre1[i]
            btm = pre2[i - 1] if i > 0 else 0

            second = max(top, btm)
            res = min(res, second)

        return res

