from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = []
        n = len(heights)
        max_area = 0

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                index = stack.pop()
                prev_height = heights[index]

                width = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, prev_height * width)

            stack.append(i)

        return max_area

