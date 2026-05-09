class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(x for x, _ in points)

        return max(x[i] - x[i - 1] for i in range(1, len(points)))
