from collections import defaultdict
from math import gcd


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        pairs = 0

        cache = defaultdict(list)
        for i, num in enumerate(nums):
            cache[num].append(i)

        for num, idx in cache.items():
            if len(idx) < 2:
                continue

            gcds = defaultdict(int)

            for i in idx:
                gcd_i = gcd(i, k)

                for gcd_j, gcd_count in gcds.items():
                    if gcd_i * gcd_j % k == 0:
                        pairs += gcd_count

                gcds[gcd_i] += 1

        return pairs

