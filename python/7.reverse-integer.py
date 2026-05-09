class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x:
            x, rem = divmod(x, 10)
            res *= 10
            res += rem * sign
        if ~(1 << 31) + 1 < res < (1 << 31):
            return res
        else:
            return 0
