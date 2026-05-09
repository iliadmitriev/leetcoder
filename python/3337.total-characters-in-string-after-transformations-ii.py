
import numpy as np

MOD = int(1e9 + 7)


def pow(A: np.ndarray, n: int):
    res = np.identity(A.shape[0], dtype=object)

    while n > 0:
        if n & 1:
            res = res @ A
            res %= MOD

        A = A @ A
        A %= MOD

        n >>= 1

    return res


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = int(1e9 + 7)
        base = ord("a")  # 97
        N = ord("z") - base + 1  # 26
        cnt = [0] * N
        res = [0] * N
        total = 0

        for c in s:
            cnt[ord(c) - base] += 1

        transform = np.zeros((N, N), dtype=object)

        for j in range(N):
            for k in range(nums[j]):
                i = (j + k + 1) % N
                transform[i, j] += 1

        transform = pow(transform, t)

        for i in range(N):
            for j in range(N):
                res[i] = (res[i] + transform[i, j] * cnt[j]) % MOD

        total = 0
        for i in range(N):
            total = (total + res[i]) % MOD

        return total

