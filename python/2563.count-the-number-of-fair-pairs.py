import bisect


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        # doesn't matter how we count a pair (i, j) or (j, i) if it is fair,
        # the only thing that matters is if we count it only once
        nums.sort()

        def countBounded(nums, bound):
            count = 0
            left, right = 0, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > bound:
                    right -= 1
                else:
                    count += right - left
                    left += 1

            return count

        return countBounded(nums, upper) - countBounded(nums, lower - 1)

