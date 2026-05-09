
class Solution {
private:
  const long long MOD = 1e9 + 7;

  long long power(long long base, long long exp, long long mod) {

    if (mod == 1) {
      return 0;
    }

    base %= mod;
    long long res = 1;

    while (exp) {
      if (exp & 1) {
        res *= base;
        res %= mod;
      }
      base *= base;
      base %= mod;
      exp >>= 1;
    }

    return res;
  }

public:
  int countGoodNumbers(long long n) {
    long odd = n / 2, even = n - odd;
    return (power(5, even, MOD) * power(4, odd, MOD)) % MOD;
  }
};