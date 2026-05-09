class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        p = i
        
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1

        q = i

        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        return p > 0 and p < q < i and i == n - 1