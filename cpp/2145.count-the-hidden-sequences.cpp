#include <vector>
using std::vector;

class Solution {
public:
  int numberOfArrays(vector<int> &differences, int lower, int upper) {
    long cur = 0, bottom = 0, top = 0;

    for (int diff : differences) {
      cur += diff;
      bottom = std::min(bottom, cur);
      top = std::max(top, cur);
    }

    long delta = top - bottom, diff = upper - lower;

    if (delta > diff) {
      return 0;
    }

    return diff - delta + 1;
  }
};