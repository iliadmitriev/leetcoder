class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if k == 1:
            return 0

        return sum(nums) % k

