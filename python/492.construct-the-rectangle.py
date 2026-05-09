import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        top = int(math.sqrt(area))

        while area % top != 0:
            top -= 1

        return [area // top, top]

