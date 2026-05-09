class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        bottom, top = 0, 0
        cur = 0

        for diff in differences:
            cur += diff
            bottom = min(bottom, cur)
            top = max(top, cur)

        delta = upper - lower
        diff = top - bottom

        if delta < diff:
            return 0

        return delta - diff + 1

