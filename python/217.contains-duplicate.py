class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        cache = set()
        for num in nums:
            if num in cache:
                return True

            cache.add(num)

        return False

