
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        sum_cache = {0: 1}
        cur_sum = 0

        for num in nums:
            cur_sum += num
            res += sum_cache.get(cur_sum - goal, 0)
            sum_cache[cur_sum] = sum_cache.get(cur_sum, 0) + 1

        return res

