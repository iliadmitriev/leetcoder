class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, n):
            cur_max = 0
            max_at_i = 0

            for j in range(i, max(-1, i - k), -1):
                cur_max = max(cur_max, arr[j])
                window = i - j + 1
                cur_sum = cur_max * window
                sub_sum = dp[(j - 1) % k]

                max_at_i = max(max_at_i, cur_sum + sub_sum)

            dp[i % k] = max_at_i

        return dp[(n - 1) % k]