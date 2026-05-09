class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            lookup = target - num
            if lookup in cache and i != cache[lookup]:
                return (i, cache[lookup])