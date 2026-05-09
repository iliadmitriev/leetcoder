#include <iostream>
#include <vector>

using std::vector;

class Solution {
private:
  bool isPrime(int num) {
    if (num <= 1) {
      return false;
    }
    if (num <= 3) {
      return true;
    }

    if (num % 2 == 0 || num % 3 == 0) {
      return false;
    }

    for (int i = 5; i * i <= num; i += 6) {
      if (num % i == 0 || num % (i + 2) == 0) {
        return false;
      }
    }

    return true;
  }

public:
  vector<int> closestPrimes(int left, int right) {
    int curMin = right - left + 1;
    int prev = -1;
    vector<int> res(2, -1);

    for (int n = left; n <= right; ++n) {
      if (!isPrime(n)) {
        continue;
      }

      if (prev == -1) {
        prev = n;
        continue;
      }

      int diff = n - prev;
      if (diff <= 2) {
        return {prev, n};
      }

      if (diff < curMin) {
        curMin = diff;
        res = {prev, n};
      }

      prev = n;
    }

    return res;
  }
};