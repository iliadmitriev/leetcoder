#include <cstdlib>
class Solution {
public:
  int mirrorDistance(int n) { return std::abs(n - rev(n)); }

private:
  int rev(int x) {
    int res = 0;

    while (x) {
      res = res * 10 + x % 10;
      x /= 10;
    }

    return res;
  }
};