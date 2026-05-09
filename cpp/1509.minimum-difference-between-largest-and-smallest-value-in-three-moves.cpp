#include <algorithm>
#include <vector>

using std::min;
using std::sort;
using std::vector;

class Solution {
public:
  int minDifference(vector<int> &nums) {
    int n = nums.size();
    if (n < 5)
      return 0;

    sort(nums.begin(), nums.end());
    int ans = nums[n - 4] - nums[0];

    for (int k = 0; k < 4; ++k) {
      ans = min(ans, nums[n - 4 + k] - nums[k]);
    }

    return ans;
  }
};