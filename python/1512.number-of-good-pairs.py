class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        res = 0
        for num in nums:
            if num in cache:
                res += cache[num]
            cache[num] += 1
        return res