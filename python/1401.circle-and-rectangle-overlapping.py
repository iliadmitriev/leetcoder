class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def dist(ax, ay, bx, by) -> int:
            return (ax - bx) ** 2 + (ay - by) ** 2

        # # the center is inside the rectangle
        # if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
        #     return True

        # # the center is above or below the rectangle
        # if x1 <= xCenter <= x2 and y1 <= yCenter <= y2 + radius:
        #     return True

        # if x1 <= xCenter <= x2 and y1 - radius <= yCenter <= y2:
        #     return True

        # # the center is to the right or to the left of the rectangle
        # if x1 <= xCenter <= x2 + radius and y1 <= yCenter <= y2:
        #     return True

        # if x1 - radius <= xCenter <= x2 and y1 <= yCenter <= y2:
        #     return True

        # # the center is (inside the 2nd order curve):
        # # in the upper left corner
        # if dist(xCenter, yCenter, x1, y2) <= radius**2:
        #     return True
        # # in the lower left corner
        # if dist(xCenter, yCenter, x1, y1) <= radius**2:
        #     return True
        # # in the upper right corner
        # if dist(xCenter, yCenter, x2, y2) <= radius**2:
        #     return True
        # # in the lower right corner
        # if dist(xCenter, yCenter, x2, y1) <= radius**2:
        #     return True
        # # otherwise
        # return False

        # calculate closest point to the center
        x = max(x1, min(x2, xCenter))
        y = max(y1, min(y2, yCenter))

        return dist(x, y, xCenter, yCenter) <= radius**2
