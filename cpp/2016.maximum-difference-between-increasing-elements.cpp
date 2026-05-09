#include <vector>
using std::vector;

class Solution {
public:
  int maximumDifference(vector<int> &nums) {
    int maxDiff = -1, mmin = std::numeric_limits<int>::max();

    for (int num : nums) {
      mmin = std::min(mmin, num);
      maxDiff = std::max(maxDiff, num - mmin);
    }

    return maxDiff > 0 ? maxDiff : -1;
  }
};