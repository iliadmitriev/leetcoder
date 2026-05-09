
MOD = int(1e9 + 7)


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        total = 1

        freq = []
        prev = ""

        for ch in word:
            if prev == ch:
                freq[-1] += 1
            else:
                freq.append(1)
                prev = ch

        total = 1
        for f in freq:
            total = (total * f) % MOD

        if len(freq) >= k:
            return total

        dp = [0] * k
        dp[0] = 1

        for f in freq:
            new_dp = [0] * k

            cur_sum = 0
            for s in range(k):
                if s > 0:
                    cur_sum = (cur_sum + dp[s - 1]) % MOD

                if s > f:
                    cur_sum = (cur_sum - dp[s - f - 1] + MOD) % MOD

                new_dp[s] = cur_sum

            dp = new_dp

        n = len(freq)
        invalid = 0

        for i in range(n, k):
            invalid = (invalid + dp[i]) % MOD

        return (total - invalid + MOD) % MOD

