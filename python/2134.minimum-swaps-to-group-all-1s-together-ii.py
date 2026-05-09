class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        onesCount = sum(nums)

        nums = nums
        left = 0
        count = 0
        n = len(nums)

        ans = len(nums) - onesCount
        for right in range(n * 2):
            count += nums[right % n] == 1

            if right - left + 1 > onesCount:
                count -= nums[left % n] == 1
                left += 1

            if right - left + 1 == onesCount:
                ans = min(ans, onesCount - count)

        return ans

