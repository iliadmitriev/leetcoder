from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack: list[int] = []

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                j = stack.pop()
                if not stack:
                    break
                water += (min(height[stack[-1]], h) - height[j]) * (i - stack[-1] - 1)
            stack.append(i)
        return water

