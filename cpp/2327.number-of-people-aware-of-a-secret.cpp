#include <vector>
using std::vector;

class Solution {
public:
  int peopleAwareOfSecret(int n, int delay, int forget) {
    const int MOD = 1e9 + 7;

    // shift days index from 1 to 0
    vector<int> dp(n, 0);
    dp[0] = 1;

    long long s = 0, res = 0;

    for (int i = delay; i < n; i++) {
      s += dp[i - delay];
      dp[i] = s % MOD;

      if (i - forget + 1 >= 0) {
        s -= dp[i - forget + 1];
        s = (s + MOD) % MOD;
      }
    }

    for (int i = n - forget; i < n; i++) {
      res = (res + dp[i]) % MOD;
    }

    return res;
  }
};