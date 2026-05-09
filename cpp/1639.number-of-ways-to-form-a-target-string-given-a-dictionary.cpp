#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  const int MOD = 1e9 + 7;

  int numWays(vector<string> &words, string target) {
    const int m = words.front().size(), n = target.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    vector<vector<int>> wc(m, vector<int>(26, 0));
    for (const string &word : words) {
      for (int i = 0; i < m; ++i) {
        wc[i][word[i] - 'a']++;
      }
    }

    for (int j = m; j >= 0; --j) {
      dp[n][j] = 1;
    }

    for (int i = n - 1; i >= 0; --i) {
      for (int j = m - 1; j >= 0; --j) {
        if (m - j < n - j) {
          break;
        }

        long long ways = 0;

        if (wc[j][target[i] - 'a'] > 0) {
          ways += long(dp[i + 1][j + 1]) * wc[j][target[i] - 'a'] % MOD;
        }

        ways += dp[i][j + 1];
        ways %= MOD;

        dp[i][j] = ways;
      }
    }

    return dp[0][0];
  }
};