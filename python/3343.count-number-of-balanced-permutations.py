from collections import Counter
from functools import cache
from math import comb


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = int(1e9 + 7)
        n = len(num)
        total = sum(map(int, num))

        # heuristic
        if total % 2 != 0:
            return 0

        target = total // 2
        odd_n = n // 2
        cnt = Counter(map(int, num))

        cnt_prefix = [0] * 10
        cur = 0
        for k in range(9, -1, -1):
            cur += cnt[k]
            cnt_prefix[k] = cur

        @cache
        def dfs(i: int, odd_left: int, odd_sum: int):
            if odd_left < 0 or odd_sum > target:
                return 0
            if i > 9:
                return int(odd_left == 0 and odd_sum == target)

            even_left = cnt_prefix[i] - odd_left

            res = 0
            for j in range(max(0, cnt[i] - even_left), min(cnt[i], odd_left) + 1):
                ways = comb(odd_left, j) * comb(even_left, cnt[i] - j) % MOD
                res += ways * dfs(i + 1, odd_left - j, odd_sum + j * i)
                res %= MOD

            return res % MOD

        return dfs(0, odd_n, 0)

