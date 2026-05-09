class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        popcount = lambda x: x.bit_count()

        # 1. first term:
        #  *  `a` or `b` is equal to `1`, but `c` is `0`
        #  *  `a` and `b` is `0`, but `c` is `1`
        # 2. second term:
        #  *  `a` and `b` is `0`, but `c` is `1` (this should be counted twice)

        return popcount((a | b) ^ c) + popcount(a & b & ~c)