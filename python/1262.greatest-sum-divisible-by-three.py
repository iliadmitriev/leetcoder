class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        total = sum(nums)

        rem = total % 3

        if rem == 0:
            return total

        # get two minimal numbers which is not divisible by 3
        # to chose one of them or two (which is less)
        v = int(1e9)
        a1, b1 = v, v  # two minimal numbers with remainder 1, a1 <= b1
        a2, b2 = v, v  # two minimal numbers with remainder 2, a2 <= b2

        for num in nums:
            if num % 3 == 1:
                if num <= a1:
                    a1, b1 = num, a1
                elif num < b1:
                    b1 = num

            elif num % 3 == 2:
                if num <= a2:
                    a2, b2 = num, a2
                elif num < b2:
                    b2 = num

        # reminder is 1 so we can chose one number with remainder 1 or two numbers with remainder 2
        if rem == 1:
            return total - min(a1, a2 + b2)

        # reminder is 2 so we can chose one number with remainder 2 or two numbers with remainder 1
        return total - min(a1 + b1, a2)

