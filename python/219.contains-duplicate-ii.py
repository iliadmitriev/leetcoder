class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and abs(i - cache[num]) <= k:
                return True
            cache[num] = i
        return False