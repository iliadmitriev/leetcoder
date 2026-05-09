#include <cmath>
#include <vector>
using std::vector;

class Solution {
private:
  const int MOD = int(1e9 + 7);

  int limit;
  int x;
  vector<vector<int>> cache;

  int dp(int n, int i) {
    if (n == 0) {
      return 1;
    }

    if (n < 0 || i > limit) {
      return 0;
    }

    if (cache[n][i] != -1) {
      return cache[n][i];
    }

    int next = std::pow(i, x);
    int res = dp(n - next, i + 1) + dp(n, i + 1);
    res %= MOD;

    return cache[n][i] = res;
  }

public:
  int numberOfWays(int n, int x) {
    this->x = x;
    this->limit = std::pow(n, 1.0 / x) + 1;
    this->cache = vector<vector<int>>(n + 1, vector<int>(this->limit + 1, -1));

    return dp(n, 1);
  }
};