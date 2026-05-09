class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cnt = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                if cnt >= 2:
                    nums.pop(i)
                else:
                    cnt += 1
                    i += 1
            else:
                cnt = 1
                i += 1
        return i