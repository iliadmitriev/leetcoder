class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        # num -> (start, end, count)
        cache: dict[int, tuple[int, int, int]] = {}

        degree = 1

        for i, num in enumerate(nums):
            if num not in cache:
                cache[num] = (i, i, 1)
            else:
                start, _, count = cache[num]
                cache[num] = (start, i, count + 1)
                degree = max(degree, count + 1)

        minLength = len(nums)

        for start, end, count in cache.values():
            if count == degree:
                minLength = min(minLength, end - start + 1)

        return minLength

