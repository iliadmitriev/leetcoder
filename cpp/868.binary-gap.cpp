#include <algorithm>

class Solution {
public:
  int binaryGap(int n) {
    while ((n & 1) == 0) {
      n >>= 1;
    }

    int maxGap = 0, start = 0;

    for (int i = 0; n; n >>= 1, i++) {
      if (n & 1) {
        maxGap = std::max(maxGap, i - start);
        start = i;
      }
    }

    return maxGap;
  }
};