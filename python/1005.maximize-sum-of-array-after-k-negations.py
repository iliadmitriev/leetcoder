class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:

        nums.sort(key=abs, reverse=True)
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

            if not k:
                break

        if k % 2:
            nums[-1] = -nums[-1]

        return sum(nums)

