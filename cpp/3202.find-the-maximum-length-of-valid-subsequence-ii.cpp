#include <vector>

using std::vector;

class Solution {
public:
  int maximumLength(vector<int> &nums, int k) {
    int maxLen = 0;
    vector<vector<int>> dp(k, vector<int>(k, 0));

    for (int num : nums) {
      num %= k;

      for (int j = 0; j < k; j++) {
        dp[num][j] = dp[j][num] + 1;
        maxLen = std::max(maxLen, dp[num][j]);
      }
    }

    return maxLen;
  }
};