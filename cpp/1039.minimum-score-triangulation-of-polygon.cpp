#include <limits>
#include <vector>

using std::vector;

class Solution {
private:
  const int INF = std::numeric_limits<int>::max();

  int dp(vector<vector<int>> &cache, const vector<int> &values, int i, int j) {
    if (j - i < 2) {
      return 0;
    }

    if (j - i == 2) {
      return values[i] * values[i + 1] * values[j];
    }

    if (cache[i][j] != -1) {
      return cache[i][j];
    }

    int res = INF;

    for (int k = i + 1; k < j; k++) {
      res =
          std::min(res, values[i] * values[k] * values[j] +
                            dp(cache, values, i, k) + dp(cache, values, k, j));
    }

    return cache[i][j] = res;
  }

public:
  int minScoreTriangulation(vector<int> &values) {
    const int n = values.size();
    vector<vector<int>> cache(n, vector<int>(n, -1));

    return dp(cache, values, 0, n - 1);
  }
};