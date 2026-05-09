#include <vector>
using std::vector;

class Solution {
public:
  int numberOfPaths(vector<vector<int>> &grid, int k) {
    const int m = grid.size(), n = grid.front().size();
    const int MOD = int(1e9) + 7;

    vector<vector<int>> dp(n + 1, vector<int>(k, 0));
    dp[1][0] =
        1; // base state for 0th (shifted + 1) column with 0 remainder count 1.

    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        vector<int> row(k, 0);

        for (int rem = 0; rem < k; rem++) {
          int nextRem = (rem + grid[r][c]) % k;
          row[rem] = (dp[c][nextRem] + dp[c + 1][nextRem]) % MOD;
        }

        dp[c + 1] = row;
      }
    }

    return dp[n][0];
  }
};