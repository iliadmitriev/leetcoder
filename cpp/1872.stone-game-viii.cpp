#include <vector>
#include <numeric>

using std::vector;

class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
      const int n = stones.size();
      vector<int> pre(n, 0);
      vector<int> dp(n + 1, 0);

      std::partial_sum(stones.begin(), stones.end(), pre.begin());

      dp[n - 1] = pre[n - 1]; // -inf

      for (int i = n - 2; i >= 0; i--) {
        dp[i] = std::max(dp[i + 1], pre[i] - dp[i + 1]);
      }

      return dp[1]; // should take one at least
    }
};