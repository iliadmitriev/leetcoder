class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:

        cnt = 0
        for num in nums:
            cnt += 1 - num & 1

            if cnt > 1:
                return True

        return False

