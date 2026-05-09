#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  long long minimumCost(string source, string target, vector<char> &original,
                        vector<char> &changed, vector<int> &cost) {

    const int INF = int(1e9), N = 26;
    const char A = 'a';

    vector<vector<int>> dp(N, vector<int>(N, INF));

    for (int i = 0; i < N; ++i) {
      dp[i][i] = 0;
    }

    for (int i = 0; i < original.size(); ++i) {
      if (dp[original[i] - A][changed[i] - A] < cost[i]) {
        continue;
      }

      dp[original[i] - A][changed[i] - A] = cost[i];
    }

    for (int k = 0; k < N; ++k) {
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
          if (dp[i][j] < dp[i][k] + dp[k][j]) {
            continue;
          }

          dp[i][j] = dp[i][k] + dp[k][j];
        }
      }
    }

    long total = 0;

    for (int i = 0; i < source.size(); ++i) {
      if (dp[source[i] - A][target[i] - A] == INF) {
        return -1;
      }

      total += dp[source[i] - A][target[i] - A];
    }

    return total;
  }
};