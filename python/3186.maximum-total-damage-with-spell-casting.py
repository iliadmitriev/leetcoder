import collections


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cnt = collections.Counter(power)

        powers = sorted(cnt.keys())

        dp = 0
        p1, p2 = 0, 0
        d1, d2, d3 = 0, 0, 0

        for pwr in powers:
            value = cnt[pwr] * pwr

            dp = max(value + d3, d2, d1)

            if pwr - p2 > 2:
                dp = max(dp, value + d2)

            if pwr - p1 > 2:
                dp = max(dp, value + d1)

            p1, p2 = pwr, p1
            d1, d2, d3 = dp, d1, d2

        return dp

