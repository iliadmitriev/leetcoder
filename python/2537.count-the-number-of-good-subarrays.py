from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        count = 0
        left = 0
        window = defaultdict(int)

        for right in range(n):
            pairs += window[nums[right]]
            window[nums[right]] += 1

            while pairs >= k:
                window[nums[left]] -= 1
                pairs -= window[nums[left]]

                left += 1

            count += left

        return count

