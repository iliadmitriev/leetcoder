class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxWidth = right - left
        maxArea = 0

        for width in range(maxWidth, 0, -1):
            maxArea = max(maxArea, min(height[left], height[right]) * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

