

import functools


def factorial(n: int, mod: int) -> list[int]:
    """Modular factorial of n numbers."""
    res = [1]

    for i in range(1, n + 1):
        res.append(res[-1] * i % mod)

    return res


def inv(x: int, mod: int) -> int:
    """Modular inverse."""
    return pow(x, mod - 2, mod)


def inv_factorial(n: int, mod: int) -> list[int]:
    """Modular inverse of factorial of n numbers."""
    return [inv(fac, mod) for fac in factorial(n, mod)]


def exp_mod(a, b, mod):
    """Modular exponentiation."""
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res


def comb_without_mod(n, k):
    if k > n:
        return 0

    if n < 2 * k:
        k = n - k

    res = 1
    for d in range(1, k + 1):
        res = res * n
        n -= 1
        res //= d
    return res


def inv_mod(a, mod):
    """Modular inverse."""
    return exp_mod(a, mod - 2, mod)


def fact_mod(n, mod):
    """Modular factorial."""
    res = 1
    for i in range(1, n + 1):
        res = res * i % mod
    return res


@functools.cache
def prod_mod(a, b, mod):
    """Modular product of all number between a and b."""
    res = 1
    for i in range(a, b + 1):
        res = res * i % mod
    return res


@functools.cache
def comb_mod(n, k, mod):
    """Modular combinations.

    https://codeforces.com/blog/entry/78873

    C(n, k)! = n! * inv(k!) * inv(n - k)!

    """
    if n - k < k:
        k = n - k

    return (prod_mod(n - k + 1, n, mod) * inv_mod(fact_mod(k, mod), mod)) % mod


MOD = int(1e9) + 7


class Solution:
    def magicalSum_V2(self, m: int, k: int, nums: list[int]) -> int:
        n = len(nums)

        # factorials of m + 1
        fac = factorial(m + 1, MOD)

        # inverse factorials of m + 1
        ifac = inv_factorial(m + 1, MOD)

        numsPow = [[1] * (m + 1) for _ in range(n)]

        for i in range(n):
            for j in range(1, m + 1):
                numsPow[i][j] = numsPow[i][j - 1] * nums[i] % MOD

        # create and init
        # f[i][j][p][q]
        # i - current index in nums
        # j - numbers used up to now
        # p - sum of numbers used up to now (number of bits)
        # q - number of numbers used up to now (number of 1s)
        f = [
            [[[0] * (k + 1) for _ in range(m * 2 + 1)] for _ in range(m + 1)]
            for _ in range(n)
        ]

        # initialize base case
        for j in range(m + 1):
            f[0][j][j][0] = numsPow[0][j] * ifac[j] % MOD

        # calculations

        for i in range(n - 1):
            for j in range(m + 1):
                for p in range(2 * m + 1):
                    for q in range(k + 1):
                        if f[i][j][p][q] == 0:
                            continue

                        q2 = (p % 2) + q
                        if q2 > k:
                            break

                        for r in range(m - j + 1):
                            p2 = (p // 2) + r
                            if p2 > 2 * m:
                                continue

                            f[i + 1][j + r][p2][q2] = (
                                f[i + 1][j + r][p2][q2]
                                + f[i][j][p][q]
                                * numsPow[i + 1][r]
                                % MOD
                                * ifac[r]
                                % MOD
                            ) % MOD

        # collect the results

        res = 0

        for p in range(2 * m + 1):
            for q in range(k + 1):
                if p.bit_count() + q == k:
                    res = (res + f[n - 1][m][p][q] * fac[m] % MOD) % MOD

        return res

    def magicalSum(self, M: int, K: int, nums: list[int]) -> int:
        @functools.cache
        def dp(m: int, k: int, i, mask) -> int:
            """
            m: how many more elements to choose (remaining elements to place into the sequence)
            k: how many more bits is needed to achive the target (remaining bits needed in final sequence)
            i: current index in nums
            mask: carry bits from binary addition of 2^index values

            """
            if m < 0 or k < 0 or m + mask.bit_count() < k:
                return 0

            if m == 0:
                return int(k == mask.bit_count())

            if i >= len(nums):
                return 0

            res = 0
            for j in range(m + 1):
                mul = comb_mod(m, j, MOD) * pow(nums[i], j, MOD) % MOD
                f2 = mask + j

                res += mul * dp(m - j, k - (f2 % 2), i + 1, f2 // 2) % MOD
                res %= MOD

            return res

        return dp(M, K, 0, 0)

