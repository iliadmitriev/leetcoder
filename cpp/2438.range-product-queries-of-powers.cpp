#include <vector>
using std::vector;

class Solution {
public:
  vector<int> productQueries(int n, vector<vector<int>> &queries) {
    const int MOD = int(1e9) + 7;

    vector<int> prefix;
    int b;

    while (n) {
      b = n & -n;
      prefix.push_back(b);
      n ^= b;
    }

    const int m = prefix.size();
    vector<vector<long>> cache(m + 1, vector<long>(m + 1, 1));

    for (int i = 0; i < m; i++) {
      cache[i][i] = prefix[i];

      for (int j = i + 1; j < m; j++) {
        cache[i][j] = cache[i][j - 1] * prefix[j] % MOD;
      }
    }

    vector<int> res;
    for (const auto &q : queries) {
      res.push_back(cache[q[0]][q[1]]);
    }

    return res;
  }
};