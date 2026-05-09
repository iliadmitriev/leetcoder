#include <string>
#include <vector>
using std::vector, std::string;

class Solution {
public:
  int findMaxForm(vector<string> &strs, int m, int n) {
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    const int len = strs.size();

    for (int i = 0; i < len; i++) {
      int zeros = std::count(strs[i].begin(), strs[i].end(), '0'),
          ones = strs[i].size() - zeros;

      for (int j = m; j >= zeros; j--) {
        for (int k = n; k >= ones; k--) {
          dp[j][k] = std::max(dp[j][k], dp[j - zeros][k - ones] + 1);
        }
      }
    }

    return dp[m][n];
  }
};