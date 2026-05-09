#include <vector>

using std::vector;

class Solution {
public:
  int nthUglyNumber(int n) {
    vector<int> dp(n);

    dp[0] = 1;

    int p2 = 0, p3 = 0, p5 = 0;

    for (int i = 1; i < n; i++) {
      dp[i] = std::min({dp[p2] * 2, dp[p3] * 3, dp[p5] * 5});

      p2 += dp[i] == dp[p2] * 2;
      p3 += dp[i] == dp[p3] * 3;
      p5 += dp[i] == dp[p5] * 5;
    }

    return dp.back();
  }
};