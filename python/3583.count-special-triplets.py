import collections


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = int(1e9) + 7
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        total = 0

        for num in nums:
            if num % 2 == 0 and num // 2 in d2:
                total += d2[num // 2]
                total %= MOD

            if num * 2 in d1:
                d2[num] += d1[num * 2]
                d2[num] %= MOD

            d1[num] += 1

        return total

