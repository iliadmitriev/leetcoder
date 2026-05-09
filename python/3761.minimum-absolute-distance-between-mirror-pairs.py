import collections


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        inf = len(nums) + 1
        dist = inf
        cache1 = collections.defaultdict(int)

        def rev(x: int) -> int:
            return int(str(x)[::-1].lstrip('0'))

        for j, num in enumerate(nums):

            if num in cache1:
                dist = min(dist, j - cache1[num])

            if dist == 1:
                return dist
            
            mun = rev(num)
            cache1[mun] = j

        if dist == inf:
            return -1
        return dist