from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        i, j = 0, 0
        mp = defaultdict(int)

        for r in range(n):
            mp[nums[r]] += 1

            while len(mp) > k:
                mp[nums[j]] -= 1

                if mp[nums[j]] == 0:
                    mp.pop(nums[j])
                j += 1
                i = j

            while mp[nums[j]] > 1:
                mp[nums[j]] -= 1
                j += 1

            if len(mp) == k:
                res += j - i + 1

        return res

