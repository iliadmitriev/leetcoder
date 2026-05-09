

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:

        f = -values[0]
        g = 0

        for i, value in enumerate(values):
            f = max(f, g + value - i)
            g = max(g, value + i)

        return f

