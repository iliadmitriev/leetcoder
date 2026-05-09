class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # two max numbers max1 > max2
        max1, max2 = 0, 0
        for num in nums:
            if max1 < num:
                max2 = max1
                max1 = num
            elif max2 < num:
                max2 = num
        return (max1 - 1) * (max2 - 1)