#include <vector>
using std::vector;

class Solution {
public:
  long long mostPoints(vector<vector<int>> &questions) {
    const int n = questions.size();
    vector<long long> dp(n + 1, 0);

    for (int i = n - 1; i >= 0; i--) {
      int next = std::min(n, i + questions[i][1] + 1);
      dp[i] = std::max(questions[i][0] + dp[next], dp[i + 1]);
    }

    return dp[0];
  }
};