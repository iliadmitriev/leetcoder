class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:

        res: list[list[int]] = []
        for i in range(rows):
            for j in range(cols):
                res.append([i, j])

        res.sort(key=lambda h: abs(h[0] - rCenter) + abs(h[1] - cCenter))

        return res

