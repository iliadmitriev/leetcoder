from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack: list[int] = []
        n = len(heights)

        for i in range(len(heights) + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                index = stack.pop()
                prev = heights[index]
                width = i - stack[-1] - 1 if stack else i

                max_rect = max(max_rect, prev * width)

            stack.append(i)

        return max_rect

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        m, n = len(matrix), len(matrix[0])
        hist = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    hist[j] = 0
                else:
                    hist[j] += 1

            max_area = max(max_area, self.largestRectangleArea(hist))

        return max_area

