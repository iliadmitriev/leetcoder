class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for y1, x1, y2, x2 in queries:
            prefix[y1][x1] += 1  # top left
            prefix[y1][x2 + 1] -= 1  # top right
            prefix[y2 + 1][x1] -= 1  # bottom left
            prefix[y2 + 1][x2 + 1] += 1  # bottom right

        acc = [[0] * n for _ in range(n)]

        for i in range(n):
            row = 0
            for j in range(n):
                row += prefix[i][j]
                acc[i][j] = row

                if i == 0:
                    continue

                acc[i][j] += acc[i - 1][j]

        return acc

