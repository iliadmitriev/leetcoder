#include <cmath>

class Solution {
public:
  bool judgeSquareSum(int c) {
    // fermat theorem all prime factors of given number
    // which can be represented as 4 * i + 3, should not occur odd
    int n = sqrt(c) + 1;

    for (int i = 2; i <= n; ++i) {

      if (c % i)
        continue;

      int cnt = 0;
      while (c % i == 0) {
        ++cnt;
        c /= i;
      }

      if (i % 4 == 3 && cnt % 2)
        return false;
    }

    return c % 4 != 3;
  }
};