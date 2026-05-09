#include <vector>
using std::vector;

class Solution {
private:
  inline int max(int a, int b) {
    if (a > b)
      return a;
    return b;
  }

public:
  int maxMoves(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid.back().size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
      dp[i][0] = 1;
    }

    int maxMoves = 0;

    for (int j = 1; j < n; j++) {
      for (int i = 0; i < m; i++) {
        if (grid[i][j] > grid[i][j - 1] && dp[i][j - 1] > 0) {
          dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1);
        }

        if (i - 1 >= 0 && grid[i][j] > grid[i - 1][j - 1] &&
            dp[i - 1][j - 1] > 0) {
          dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
        }

        if (i + 1 < m && grid[i][j] > grid[i + 1][j - 1] &&
            dp[i + 1][j - 1] > 0) {
          dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1);
        }

        maxMoves = max(maxMoves, dp[i][j] - 1);
      }
    }

    return maxMoves;
  }
};