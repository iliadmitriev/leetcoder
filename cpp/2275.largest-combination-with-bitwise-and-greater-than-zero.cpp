#include <iostream>
#include <vector>

using std::vector;

#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
#pragma GCC optimize("O3", "unroll-loops")
#pragma GCC optimize("-ffloat-store")

auto init = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  return 0;
}();

class Solution {
public:
  int largestCombination(vector<int> &candidates) {
    int maxCounter = 0;

    for (int bit = 0; bit < 24; bit++) {
      int mask = 1 << bit;
      int counter = 0;

      for (auto num : candidates) {
        if ((num & mask) == 0) {
          continue;
        }

        counter++;
      }

      maxCounter = std::max(maxCounter, counter);
    }

    return maxCounter;
  }
};