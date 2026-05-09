import collections


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        maxUniq = 0

        left = 0
        cur = 0
        win = collections.defaultdict(int)
        for right in range(len(nums)):
            cur += nums[right]

            win[nums[right]] += 1

            while win[nums[right]] > 1:
                cur -= nums[left]
                win[nums[left]] -= 1
                left += 1

            maxUniq = max(maxUniq, cur)

        return maxUniq

