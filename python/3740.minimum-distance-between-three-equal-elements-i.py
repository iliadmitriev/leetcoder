import collections as col

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        min_dist = 2 * n + 1
        cache = col.defaultdict(list[int])

        for i, x in enumerate(nums):
            cache[x].append(i)

            if len(cache[x]) >= 3:
                min_dist = min(min_dist, 2 * (cache[x][-1] - cache[x][-3]))

        if min_dist < 2 * n:
            return min_dist

        return -1
        