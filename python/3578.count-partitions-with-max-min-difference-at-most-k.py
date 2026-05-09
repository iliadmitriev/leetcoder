import collections


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = int(10**9) + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        # for r in range(1, n + 1):
        #     mmax = nums[r - 1]
        #     mmin = nums[r - 1]
        #     for l in range(r, 0, -1):
        #         mmax = max(mmax, nums[l - 1])
        #         mmin = min(mmin, nums[l - 1])
        #         if mmax - mmin <= k:
        #             dp[r] += dp[l - 1]
        #             dp[r] %= MOD
        #         else:
        #             break
        # return dp[n]

        qMin = collections.deque()
        qMax = collections.deque()
        prefix = [0] * (n + 1)

        prefix[0] = 1
        j = 0

        for i in range(n):
            while qMax and nums[qMax[-1]] <= nums[i]:
                qMax.pop()
            qMax.append(i)

            while qMin and nums[qMin[-1]] >= nums[i]:
                qMin.pop()
            qMin.append(i)

            while j < i and nums[qMax[0]] - nums[qMin[0]] > k:
                if qMax[0] == j:
                    qMax.popleft()
                if qMin[0] == j:
                    qMin.popleft()
                j += 1

            dp[i + 1] = (prefix[i] - prefix[j - 1] + MOD) % MOD
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % MOD

        return dp[n]

