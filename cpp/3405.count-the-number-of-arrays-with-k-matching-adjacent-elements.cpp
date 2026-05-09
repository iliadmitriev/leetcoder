class Solution {
private:
  const int MOD = 1e9 + 7;

  // factorial with modular arithmetic
  int factMod(int n, int mod) {
    long res = 1;

    for (int i = 2; i <= n; i++) {
      res = (res * i) % mod;
    }

    return res;
  }

  // modular exponentiation
  int expMod(int base, int exp, int mod) {
    long res = 1;

    long b = base, e = exp;

    while (e) {
      if (e & 1) {
        res = (res * b) % mod;
      }
      b = (b * b) % mod;
      e >>= 1;
    }

    return res;
  }

  // modular inverse
  int invMod(int a, int mod) { return expMod(a, mod - 2, mod); }

  // modular combinations count
  // C(n, k) = n! / (k! * (n - k)!) = n! * inv(k!) * inv(n - k)!
  int combMod(int n, int k, int mod) {
    long res = factMod(n, mod);

    res = (res * invMod(factMod(k, mod), mod)) % mod;
    res = (res * invMod(factMod(n - k, mod), mod)) % mod;

    return res;
  }

public:
  int countGoodArrays(int n, int m, int k) {
    // C(m - 1, n - k - 1) * (m - 1) ^ (n - k - 1) * m

    long res = combMod(n - 1, n - k - 1, MOD);
    res = (res * expMod(m - 1, n - k - 1, MOD)) % MOD;
    res = (res * m) % MOD;

    return res;
  }
};