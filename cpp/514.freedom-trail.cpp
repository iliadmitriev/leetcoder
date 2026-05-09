#include <map>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int findRotateSteps(string ring, string key) {
    int n = ring.size(), m = key.size();

    map<char, vector<int>> ring2pos;
    for (int i = 0; i < n; i++) {
      ring2pos[ring[i]].push_back(i);
    }

    vector<int> base(n);
    iota(base.begin(), base.end(), 0);

    vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));
    for (int j = 0; j < n; j++) {
      dp[m][j] = 0;
    }

    for (int i = m - 1; i >= 0; i--) {
      const vector<int> &pos = (i == 0 ? base : ring2pos[key[i - 1]]);
      for (auto k : pos) {
        for (auto j : ring2pos[key[i]]) {
          int step = 1 + min(abs(k - j), n - abs(k - j));
          dp[i][k] = min(dp[i][k], dp[i + 1][j] + step);
        }
      }
    }

    return dp[0][0];
  }
};