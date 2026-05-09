from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = int(s, 10)

        # pos = pow(10, len(s))
        #
        # def dp(num: int, cur: int, pos: int) -> int:
        #     if cur > finish or pos > finish * 10:
        #         return 0
        #
        #     res = 0
        #     if start <= cur and num > 0:
        #         res += 1
        #
        #     for i in range(limit + 1):
        #         res += dp(i, pos * i + cur, pos * 10)
        #
        #     return res
        #
        # return dp(0, suffix, pos) + int(start <= suffix and suffix <= finish)

        # def dp(x: int, limit: int) -> int:
        #     value = str(x)
        #     size = len(value)
        #     count = 0
        #
        #     for i in range(size):
        #         if int(value[i]) > limit:
        #             count += (limit + 1) ** (size - i)
        #             return count
        #
        #         count += int(value[i]) * (limit + 1) ** (size - i - 1)
        #
        #     return count
        #
        # start -= 1
        #
        # res = dp(finish, limit) - dp(start, limit)
        #
        # return res

        startStr = str(start)
        finishStr = str(finish)
        n = len(finishStr)
        startStr = startStr.zfill(n)

        prefix_len = n - len(s)

        @cache
        def dfs(i: int, low: bool, high: bool) -> int:
            if i == n:
                return 1

            lo = int(startStr[i]) if low else 0
            hi = int(finishStr[i]) if high else 9

            if i >= prefix_len:
                x = int(s[i - prefix_len])
                if lo <= x <= min(hi, limit):
                    return dfs(
                        i + 1,
                        low and x == lo,
                        high and x == hi,
                    )

                return 0

            res = 0
            for x in range(lo, min(hi, limit) + 1):
                res += dfs(
                    i + 1,
                    low and x == lo,
                    high and x == hi,
                )

            return res

        return dfs(0, True, True)

