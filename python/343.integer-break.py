class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(num: int) -> int:
            if n == 1:
                return 1

            res = 0 if num == n else num

            for i in range(1, num):
                res = max(res, dp(i) * dp(num - i))

            return res

        return dp(n)