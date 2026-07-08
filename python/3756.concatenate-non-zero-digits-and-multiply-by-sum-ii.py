MOD = int(1e9 + 7)
MAX_SIZE = int(1e5 + 1)  # max s length
POW10 = [0] * MAX_SIZE
POW10[0] = 1  # 10^0 = 1

for i in range(1, MAX_SIZE):
    POW10[i] = (POW10[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        m = len(queries)

        cnt = [0] * (n + 1)  # count skipping 0's
        z = [0] * (n + 1)  # prefix sum of all non 0's
        p = [0] * (n + 1)  # prefix product s * x
        res = [0] * m

        for i in range(1, n + 1):
            d = int(s[i - 1])

            z[i] = z[i - 1] + d

            if d > 0:
                p[i] = (p[i - 1] * 10 + d) % MOD
                cnt[i] = cnt[i - 1] + 1
            else:
                p[i] = p[i - 1]
                cnt[i] = cnt[i - 1]

        for i, (l, r) in enumerate(queries):
            r += 1 # right bound not inclusive

            length = cnt[r] - cnt[l]
            p_cur = (p[r] - p[l] * POW10[length] % MOD + MOD) % MOD
            s_cur = z[r] - z[l]

            res[i] = p_cur * s_cur % MOD

        return res
