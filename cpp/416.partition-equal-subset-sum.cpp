#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  bool canPartition(vector<int> &nums) {
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    if (total % 2 != 0) {
      return false;
    }

    int target = total / 2;
    std::vector<bool> dp(target + 1, false);
    dp[0] = true;

    for (int num : nums) {
      if (dp[target]) {
        return true;
      }

      for (int j = target; j >= num; j--) {
        dp[j] = dp[j] || dp[j - num];
      }
    }
    return dp[target];
  }
};