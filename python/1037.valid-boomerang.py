class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points

        if x1 == x2 == x3 or y1 == y2 == y3:
            return False

        return (x1 - x3) * (y2 - y3) != (x2 - x3) * (y1 - y3)

