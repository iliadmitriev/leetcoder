class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res, win = 0, 0

        for i in range(0, k):
            win += nums[i]

        res = win

        for i in range(k, len(nums)):
            win += nums[i]
            win -= nums[i - k]

            res = max(res, win)

        return res / k