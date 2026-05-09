class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:

        res = 0

        for i in range(32):
            counter = 0

            for j in range(len(nums)):
                if nums[j] >> i & 1:
                    counter += 1

                if counter >= k:
                    res += 1 << i
                    break

        return res

