class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, max2 = 1, 1
        min1, min2 = 10**4, 10**4

        for n in nums:
            if max1 < n:
                max1, max2 = n, max1
            elif max2 < n:
                max2 = n

            if min1 > n:
                min1, min2 = n, min1
            elif min2 > n:
                min2 = n

        return (max1 * max2) - (min1 * min2)