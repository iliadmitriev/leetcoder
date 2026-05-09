#include <vector>

using namespace std;

class Solution {
public:
  int longestIdealString(string s, int k) {
    vector<int> dp(26, 0);
    int n = s.size();

    for (int i = 0; i < n; ++i) {
      int cur = s[i] - 'a';

      int temp = 0;
      for (int j = max(0, cur - k); j < min(26, cur + k + 1); j++) {
        temp = max(temp, dp[j] + 1);
      }
      dp[cur] = temp;
    }

    return *max_element(dp.begin(), dp.end());
  }
};