#include <cstdlib>
#include <vector>
using std::vector;

class Solution {
public:
  int maxAdjacentDistance(vector<int> &nums) {
    const int n = nums.size();
    int maxAbs = std::abs(nums[0] - nums[n - 1]);

    for (int i = 1; i < n; i++) {
      maxAbs = std::max(maxAbs, std::abs(nums[i] - nums[i - 1]));
    }

    return maxAbs;
  }
};