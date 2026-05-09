class Solution {
private:
  bool isPrime(int n) {
    if (n < 2) {
      return false;
    }

    if (n < 4) {
      return true;
    }

    if (n % 2 == 0) {
      return false;
    }

    for (int i = 3; i * i <= n; i += 2) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

public:
  int numPrimeArrangements(int n) {
    static const int MOD = int(1e9) + 7;

    int primes = 0, notPrimes = 0;

    for (int i = 1; i <= n; i++) {
      if (isPrime(i)) {
        primes++;
      }
    }

    notPrimes = n - primes;

    long long res = 1L;

    for (int i = 2; i <= primes; i++) {
      res *= i;
      res %= MOD;
    }

    for (int i = 2; i <= notPrimes; i++) {
      res *= i;
      res %= MOD;
    }

    return res;
  }
};