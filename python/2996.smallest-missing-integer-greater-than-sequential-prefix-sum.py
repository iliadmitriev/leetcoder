class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        uniq = set(nums)
        pref = nums[0]
        i = 1
        n = len(nums)
        
        while i < n and nums[i - 1] + 1 == nums[i]:
            pref += nums[i]
            i += 1

        while pref in uniq:
            pref += 1

        return pref