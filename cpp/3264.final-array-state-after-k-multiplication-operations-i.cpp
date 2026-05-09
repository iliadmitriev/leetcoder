#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> getFinalState(vector<int> &nums, int k, int multiplier) {
    for (; k; k--) {
      auto minEl = std::min_element(nums.begin(), nums.end());
      *minEl *= multiplier;
    }

    return nums;
  }
};