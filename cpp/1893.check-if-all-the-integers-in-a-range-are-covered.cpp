#include <vector>
using std::vector;

class Solution {
public:
  bool isCovered(vector<vector<int>> &ranges, int left, int right) {
    vector<int> covered(52, 0);
    for (const auto &r : ranges) {
      covered[r[0]]++;
      covered[r[1] + 1]--;
    }

    int overlap = 0;
    for (int i = 1; i <= right; i++) {
      overlap += covered[i];

      if (left <= i && overlap == 0) {
        return false;
      }
    }

    return true;
  }
};