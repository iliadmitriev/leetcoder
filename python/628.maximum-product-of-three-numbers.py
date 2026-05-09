class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max1, max2, max3 = sorted(nums[:3])

        min1, min2 = sorted(nums[:2], reverse=True)

        for num in nums:
            # update max
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # update min
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(
            max1 * max2 * max3,
            max1 * min1 * min2,
        )

