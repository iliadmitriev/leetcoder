class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        SIZE = 30
        MOD = int(1e9 + 7)

        res = [0] * k
        bits = [0] * SIZE
        base = [1 << i for i in range(SIZE)]

        for num in nums:
            for i, b in enumerate(base):
                if num & b:
                    bits[i] += 1

        for i in range(SIZE):
            for j in range(min(k, bits[i])):
                res[j] += 1 << i

        return reduce(lambda r, x: (r + x * x) % MOD, res, 0)
