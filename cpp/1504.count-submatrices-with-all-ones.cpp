#include <vector>
using std::vector;

class Solution {
public:
  int numSubmat(vector<vector<int>> &mat) {
    const int m = mat.size(), n = mat.front().size();

    vector<int> heights(n, 0);
    vector<int> dp(n, 0);

    int total = 0, stack = -1;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1) {
          heights[j]++;
        } else {
          heights[j] = 0;
        }
      }

      stack = -1;
      for (int j = 0; j < n; j++) {
        while (stack >= 0 && heights[stack] >= heights[j]) {
          stack--;
        }

        int prev = stack >= 0 ? dp[stack] : 0;

        dp[j] = prev + (j - stack) * heights[j];
        total += dp[j];

        stack = j;
      }
    }

    return total;
  }
};