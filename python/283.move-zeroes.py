class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 0
        
        while i <= (len(nums) - 1):
            if j > (len(nums) - 1):
                nums[i] = 0
                i += 1
                continue
        
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
