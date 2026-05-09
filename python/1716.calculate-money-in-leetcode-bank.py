class Solution:
    def totalMoney(self, n: int) -> int:
        week, rest = divmod(n, 7)

        # arithmetic progression of weeks
        # 1 + ... + 7 = 28 
        # 2 + ... + 8 = 35 (+7)
        # 3 + ... + 9 = 42 (+7)
        #     ...
        # w+1 + ... w+rest = 28 + (w - 1) * 7

        # S = k * (first + last) // 2

        first = 28
        last = 28 + (week - 1) * 7
        res = week * (first + last) // 2

        # last week the rest of the days
        # first = w + 1
        # last = w + rest
        res += rest * (week + 1 + week + rest) // 2

        return res

