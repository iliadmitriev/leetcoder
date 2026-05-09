class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        N = 26
        MOD = int(1e9 + 7)
        count = [0] * N

        for c in s:
            count[ord(c) - ord("a")] += 1

        full, left = t // N, t % N

        for _ in range(full):
            tmp = count[N - 1]

            for i in range(N - 1, 0, -1):
                count[i] = (count[i] + count[i - 1]) % MOD

            count[0] = (count[0] + tmp) % MOD
            count[1] = (count[1] + tmp) % MOD

        for i in range(N - 1, N - left - 1, -1):
            count[i] = (count[i] + count[i]) % MOD

        return sum(count) % MOD

