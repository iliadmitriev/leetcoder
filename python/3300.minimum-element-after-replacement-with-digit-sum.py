class Solution:
    def minElement(self, nums: list[int]) -> int:
        def digit(x: int) -> int:
            s = 0
            while x > 0:
                x, d = divmod(x, 10)
                s += d
            return s

        return min(map(digit, nums))
        