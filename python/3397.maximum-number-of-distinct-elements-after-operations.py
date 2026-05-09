class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        if 2 * k + 1 > len(nums):
            return len(nums)

        nums.sort()

        count = 0
        prev = nums[0] - k - 1

        for cur in nums:
            if prev < cur - k:
                prev = cur - k
                count += 1
            elif prev < cur + k:
                prev += 1
                count += 1

        return count

