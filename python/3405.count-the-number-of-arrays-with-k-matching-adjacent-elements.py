

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


def comb_mod(n, k, mod):
    """Modular combinations.

    https://codeforces.com/blog/entry/78873

    C(n, k)! = n! * inv(k!) * inv(n - k)!

    """
    return (
        fact_mod(n, mod)
        * inv_mod(fact_mod(k, mod), mod)
        * inv_mod(fact_mod(n - k, mod), mod)
    ) % mod


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = int(1e9 + 7)

        c = comb_mod(n - 1, n - k - 1, MOD)
        return c * exp_mod(m - 1, n - k - 1, MOD) * m % MOD

