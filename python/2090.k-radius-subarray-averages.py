class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) <= 2 * k:
        #     return [-1] * len(nums)

        res = [-1] * len(nums)
        window = sum(nums[:(2 * k)])
        for i in range(k, len(nums) - k):
            window += nums[i + k]
            res[i] = window // (2 * k + 1)
            window -= nums[i - k]
        return res