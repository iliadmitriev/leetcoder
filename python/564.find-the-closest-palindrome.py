class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        m = len_n // 2 if len_n % 2 else len_n // 2 - 1

        left = int(n[: m + 1])

        candidates = [
            self.halfToPalindrome(left, len_n % 2 == 0),
            self.halfToPalindrome(left - 1, len_n % 2 == 0),
            self.halfToPalindrome(left + 1, len_n % 2 == 0),
            10 ** (len_n - 1) - 1,  # 999..9999
            10**len_n + 1,  # 10000..01
        ]

        int_n = int(n)
        res = 0
        diff = float("inf")
        for cand in candidates:
            if cand == int_n:
                continue

            if abs(cand - int_n) < diff:
                diff = abs(cand - int_n)
                res = cand

            elif abs(cand - int_n) == diff:
                res = min(res, cand)

        return str(res)

    @staticmethod
    def halfToPalindrome(left: int, even: bool) -> int:
        res = left

        if not even:  # shift right if it's odd
            left //= 10

        while left:
            left, digit = divmod(left, 10)
            res *= 10
            res += digit

        return res

