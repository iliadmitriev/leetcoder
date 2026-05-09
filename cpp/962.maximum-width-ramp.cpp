#include <vector>
using std::vector;

class Solution {
public:
  int maxWidthRamp(vector<int> &nums) {
    int n = nums.size();

    vector<int> prefixMax(n);
    int cumMax = nums.back();
    for (int i = n - 1; i >= 0; i--) {
      cumMax = std::max(cumMax, nums[i]);
      prefixMax[i] = cumMax;
    }

    int ramp = 0, j = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] > prefixMax[i]) {
        continue;
      }

      while (j < n && nums[i] <= prefixMax[j]) {
        j++;
      }

      ramp = std::max(ramp, j - i - 1);
    }

    return ramp;
  }
};