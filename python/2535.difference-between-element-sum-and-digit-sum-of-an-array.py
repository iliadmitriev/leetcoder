class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        def digitSum(n: int) -> int:
            s = 0
            while n:
                n, r = divmod(n, 10)
                s += r
            return s

        return abs(sum(nums) - sum(map(digitSum, nums)))

