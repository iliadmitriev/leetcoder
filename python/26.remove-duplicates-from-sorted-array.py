class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i - 1]
                k += 1
        nums[k] = nums[-1]
        return k + 1


