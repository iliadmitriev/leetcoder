def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        cache = {}

        def dp(mask, op):
            if mask in cache:
                return cache[mask]

            cache[mask] = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue

                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * gcd(nums[i], nums[j])
                    cache[mask] = max(
                        cache[mask],
                        score + dp(new_mask, op + 1)
                    )

            return cache[mask]

        return dp(0, 1)