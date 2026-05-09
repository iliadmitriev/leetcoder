from itertools import accumulate


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        @cache
        def get_cost(base):
            return sum(c * abs(num - base) for num, c in zip(nums, cost))
        
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if get_cost(mid) > get_cost(mid + 1):
                left = mid + 1
            else:
                right = mid

        return get_cost(left)
