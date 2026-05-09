from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        total = 0
        cache = defaultdict(int)
        n = len(nums)

        cur = 0
        cache[0] = 1

        for right in range(n):
            cur += int(nums[right] % modulo == k)
            leftMod = (cur - k + modulo) % modulo
            total += cache[leftMod]
            cache[cur % modulo] += 1

        return total

