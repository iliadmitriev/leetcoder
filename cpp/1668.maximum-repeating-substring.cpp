#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  int maxRepeating(string sequence, string word) {
    const int n = sequence.size(), m = word.size();
    int maxRepeat = 0;
    vector<int> dp(n + 1, 0);

    for (int i = m; i <= n; i++) {
      if (sequence.compare(i - m, m, word) == 0) {
        dp[i] = dp[i - m] + 1;
        maxRepeat = std::max(maxRepeat, dp[i]);
      }
    }

    return maxRepeat;
  }
};