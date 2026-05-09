class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        if k == 0:
            return len(set(nums))

        n = len(nums)
        count = 1
        j = 0

        nums.sort()

        for i in range(n):
            if nums[i] - nums[j] <= k:
                continue

            count += 1
            j = i

        return count

