class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        even, odd, alter1, alter2 = 0, 0, 0, 0

        for num in nums:
            if num % 2 == 0:
                even += 1
                alter1 = 1 + alter2
            else:
                odd += 1
                alter2 = 1 + alter1

        return max(even, odd, alter1, alter2)

