class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        snums = sorted(nums)
        mid = snums[len(snums) // 2]
        res = reduce(lambda x, y: x + abs(mid - y), nums, 0)
        return res