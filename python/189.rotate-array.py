class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # case when rotated version == source version
        if k % len(nums) == 0:
            return
        
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
