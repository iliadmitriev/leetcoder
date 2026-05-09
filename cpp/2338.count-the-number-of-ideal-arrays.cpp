#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

#include <stdexcept> // for std::invalid_argument
#include <tuple>     // for std::tuple

// Extended Euclidean Algorithm to find modular inverse
std::tuple<int, int, int> extended_gcd(int a, int b) {
  if (a == 0) {
    return std::make_tuple(b, 0, 1);
  } else {
    auto [g, x, y] = extended_gcd(b % a, a);
    return std::make_tuple(g, y - (b / a) * x, x);
  }
}

// Function to compute modular inverse
int mod_inverse(int a, int m) {
  auto [g, x, y] = extended_gcd(a, m);
  if (g != 1) {
    throw std::invalid_argument("Modular inverse doesn't exist");
  } else {
    return (x % m + m) % m; // Ensure positive result
  }
}

// Modular exponentiation function
long mod_exp(long base, long exponent, int modulus) {
  if (modulus <= 0) {
    throw std::invalid_argument("Modulus must be positive");
  }

  // Handle negative exponent
  if (exponent < 0) {
    int inverse = mod_inverse(base, modulus);
    return mod_exp(inverse, -exponent, modulus);
  }

  // Handle positive exponent with fast exponentiation
  long result = 1;
  base = base % modulus; // Ensure base is within modulus

  while (exponent > 0) {
    // If exponent is odd, multiply result with base
    if (exponent % 2 == 1) {
      result = (result * base) % modulus;
    }

    // exponent must be even now
    exponent = exponent >> 1; // exponent = exponent / 2
    base = (base * base) % modulus;
  }

  return result;
}

const int MOD = int(1e9) + 7;

class Solution {
private:
  // get factorize and calculate factors frequency for each number
  // in range [1,limit]
  vector<vector<int>> getFactorsCount(int limit) {
    vector<vector<int>> factorsCount(limit + 1);
    vector<int> primes(limit + 1, 0); // smallest prime factor (spf)

    // precalculate smallest prime factor for each number
    for (int num = 2; num <= limit; num++) {
      if (primes[num]) {
        continue;
      }

      for (int j = num; j <= limit; j += num) {
        if (!primes[j]) {
          primes[j] = num;
        }
      }
    }

    for (int num = 2; num <= limit; num++) {
      int spf = primes[num];
      int value = num;
      unordered_map<int, int> factors;

      while (value > 1) {
        factors[spf]++;
        value /= spf;
        spf = primes[value];
      }

      for (auto [factor, count] : factors) {
        factorsCount[num].push_back(count);
      }
    }

    return factorsCount;
  }

  // calculate combinations of k elements from n
  // fast method
  // with modular
  long long getCombinations(int n, int k) {
    long long r = 1;
    int mul = n, div = 1;

    for (int i = 0; i < k; i++) {
      mul = n - i;
      r *= mul;
      r %= MOD;

      div = i + 1;
      r *= mod_exp(div, -1, MOD);
      r %= MOD;
    }

    return r;
  }

  // greatest common divisor
  int gcd(int a, int b) {

    while (b != 0) {
      int rem = a % b;
      a = b;
      b = rem;
    }

    return a;
  }

public:
  int idealArrays(int n, int maxValue) {
    const vector<vector<int>> &factorsCount = getFactorsCount(maxValue);
    long long total = 0;

    for (int num = 1; num <= maxValue; num++) {
      long long combinations = 1;

      for (auto count : factorsCount[num]) {
        combinations *= getCombinations(n - 1 + count, count);
        combinations %= MOD;
      }

      total += combinations;
      total %= MOD;
    }

    return total;
  }
};