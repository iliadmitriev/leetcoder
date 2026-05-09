from collections import Counter, defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        counter = Counter(nums)
        win = defaultdict(int)

        left = 0

        for right in range(n):
            win[nums[right]] += 1

            while len(win) == len(counter):
                count += n - right

                win[nums[left]] -= 1
                if win[nums[left]] == 0:
                    del win[nums[left]]

                left += 1

        return count

