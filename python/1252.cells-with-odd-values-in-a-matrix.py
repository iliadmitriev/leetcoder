class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for i, j in indices:
            rows[i] ^= 1
            cols[j] ^= 1

        rowOdd, rowEven = 0, 0
        colOdd, colEven = 0, 0

        for r in rows:
            rowOdd += r
            rowEven += 1 - r

        for c in cols:
            colOdd += c
            colEven += 1 - c

        return rowOdd * colEven + rowEven * colOdd

