from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        maxSubSum = 0

        cur = defaultdict(int)
        curSum = 0

        for i, num in enumerate(nums):
            cur[num] += 1
            curSum += num

            if i >= k:
                cur[nums[i - k]] -= 1
                curSum -= nums[i - k]

                if cur[nums[i - k]] == 0:
                    del cur[nums[i - k]]

            if i >= k - 1 and len(cur) == k:
                maxSubSum = max(maxSubSum, curSum)

        return maxSubSum

