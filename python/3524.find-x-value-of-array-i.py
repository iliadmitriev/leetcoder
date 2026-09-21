class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            n = len(nums)
            return [n * (n + 1) // 2]

        dp = [0] * k
        res = [0] * k

        for num in nums:
            tmp = [0] * k
            tmp[num % k] += 1

            for r in range(k):
                if dp[r] > 0:
                    x = (r * num) % k
                    tmp[x] += dp[r]

            dp = tmp
            for r in range(k):
                res[r] += dp[r]

        return res
        