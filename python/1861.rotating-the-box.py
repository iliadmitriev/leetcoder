STONE = "#"
OBSTACLE = "*"
EMPTY = "."


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m, n = len(box), len(box[0])
        rotated = [[EMPTY] * m for _ in range(n)]

        for i, row in enumerate(box):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == STONE:
                    rotated[k][m - i - 1] = STONE
                    k -= 1
                elif row[j] == OBSTACLE:
                    rotated[j][m - i - 1] = OBSTACLE
                    k = j - 1
                elif row[j] == EMPTY:
                    pass

        return rotated

