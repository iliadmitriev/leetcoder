class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxArea = 0
        maxDiagonal = 0

        for a, b in dimensions:
            if maxDiagonal < a * a + b * b:
                maxDiagonal = a * a + b * b
                maxArea = a * b
            elif maxDiagonal == a * a + b * b:
                maxArea = max(maxArea, a * b)

        return maxArea

