from collections import Counter


class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        freq = Counter(nums)

        def comb(n: int, k: int) -> int:
            if n < k:
                return 0

            if n < 2 * k:
                k = n - k

            res = 1
            for d in range(1, k + 1):
                res *= n
                res //= d
                n -= 1

            return res

        total = comb(len(nums), 3)
        for v in freq.values():
            if v < 2:
                continue

            twoSame = (len(nums) - v) * comb(v, 2)
            treeSame = comb(v, 3)
            total -= twoSame + treeSame

        return total

