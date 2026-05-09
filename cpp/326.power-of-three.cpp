#include <cmath>
class Solution {
public:
  bool isPowerOfThree(int n) {
    if (n <= 0) {
      return false;
    }

    double x = std::log10(n) / std::log10(3);
    double diff = std::fabs(std::round(x) - x);

    return diff < 1e-11;
  }
};