#include <vector>
using std::vector;

class Solution {
public:
  int getMaximumGenerated(int n) {
    if (n < 2) {
      return n;
    }

    vector<int> dp(n + 1, 0);
    dp[0] = 0, dp[1] = 1;
    int ansMax = 1;

    for (int i = 1; i <= n / 2; i++) {
      dp[2 * i] = dp[i];
      ansMax = std::max(ansMax, dp[2 * i]);

      if (2 * i + 1 <= n) {
        dp[2 * i + 1] = dp[i] + dp[i + 1];
        ansMax = std::max(ansMax, dp[2 * i + 1]);
      }
    }

    return ansMax;
  }
};