

from collections import defaultdict


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        remainder = grid[0][0] % x
        m, n = len(grid), len(grid[0])
        buf = defaultdict(int)
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != remainder:
                    return -1

                buf[grid[i][j] // x] += 1

        mn, mx = min(buf), max(buf)
        buf2 = []

        for num in range(mn, mx + 1):
            if num not in buf:
                continue

            buf2.extend([num] * buf[num])

        mid = buf2[len(buf2) // 2]

        for num in buf2:
            ans += abs(num - mid)

        return ans

