class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def gen_perm(nums: List[int], curr: int = 0):
            if len(nums) - 1 == curr:
                result.append(nums.copy())
                return

            for i in range(curr, len(nums)):
                nums[curr], nums[i] = nums[i], nums[curr]
                gen_perm(nums, curr + 1)
                nums[curr], nums[i] = nums[i], nums[curr]
        gen_perm(nums)
        return result