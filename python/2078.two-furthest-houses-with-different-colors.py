class Solution:
    def maxDistance(self, colors: list[int]) -> int:

        n = len(colors)

        left = 0
        right = n - 1

        while left < n and colors[left] == colors[n - 1]:
            left += 1

        while right >= 0 and colors[right] == colors[0]:
            right -= 1

        return max(right, n - left - 1)
