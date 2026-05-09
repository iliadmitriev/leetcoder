#include <array>
#include <cmath>
using std::array;

class Solution {
private:
  typedef array<int, 10> A10;

  A10 count(int n) {
    A10 cnt = {0};
    while (n) {
      cnt[n % 10]++;
      n /= 10;
    }
    return cnt;
  }

public:
  bool reorderedPowerOf2(int n) {
    A10 f = count(n);

    int m = std::min(int(1e9), int(std::pow(10, std::ceil(std::log10(n)))));

    for (int x = 1; x <= m; x <<= 1) {

      if (f == count(x)) {
        return true;
      }
    }

    return false;
  }
};