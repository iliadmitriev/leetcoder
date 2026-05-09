class Solution {
private:
  // count combinations for C(k + 3 - 1, 3 - 1)
  // = C(k + 2, 2) = (k + 1) * (k + 2) / 2
  long long countComb(int k) {
    if (k < 0) {
      return 0;
    }

    return long(k + 1) * (k + 2) / 2;
  }

public:
  long long distributeCandies(int n, int limit) {
    if (limit * 3 < n) {
      return 0;
    }

    if (limit * 3 == n) {
      return 1;
    }

    // total combinations without limits
    long long total = countComb(n);

    // remove combinations with one limit violated
    total -= 3 * countComb(n - 1 * (limit + 1));

    // add back combinations with two limits violated
    total += 3 * countComb(n - 2 * (limit + 1));

    // remove combinations with three limits violated
    total -= 3 * countComb(n - 3 * (limit + 1));

    return total;
  }
};