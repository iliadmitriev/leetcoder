class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        for j in range(n):
            if nums[i] * k < nums[j]:
                i += 1

        return i
