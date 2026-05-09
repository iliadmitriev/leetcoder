class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        xa, ya = max(x1, x3), max(y1, y3)
        xb, yb = min(x2, x4), min(y2, y4)

        return xa < xb and ya < yb

