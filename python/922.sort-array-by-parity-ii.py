class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2:
                res[odd] = nums[i]
                odd += 2
            else:
                res[even] = nums[i]
                even += 2
        return res