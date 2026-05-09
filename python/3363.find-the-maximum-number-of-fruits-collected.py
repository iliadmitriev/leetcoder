class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        total = 0

        for i in range(n):
            total += fruits[i][i]

        prev, cur = [0] * n, [0] * n

        prev[n - 1] = fruits[0][n - 1]
        for i in range(1, n - 1):
            for j in range(max(n - 1 - i, i + 1), n):
                cand = prev[j]

                if j - 1 >= 0:
                    cand = max(cand, prev[j - 1])
                if j + 1 < n:
                    cand = max(cand, prev[j + 1])

                cur[j] = fruits[i][j] + cand

            prev, cur = cur, prev

        total += prev[n - 1]

        prev, cur = [0] * n, [0] * n

        prev[n - 1] = fruits[n - 1][0]
        for i in range(1, n - 1):
            for j in range(max(n - 1 - i, i + 1), n):
                cand = prev[j]

                if j - 1 >= 0:
                    cand = max(cand, prev[j - 1])
                if j + 1 < n:
                    cand = max(cand, prev[j + 1])

                cur[j] = fruits[j][i] + cand

            prev, cur = cur, prev

        total += prev[n - 1]

        return total

